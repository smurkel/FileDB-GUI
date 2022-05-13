import imgui
from imgui.integrations.glfw import GlfwRenderer
import config as cfg
import file_handler

impl = None

def start(window):
    global impl
    imgui.create_context()
    impl = GlfwRenderer(window)

def onupdate():
    impl.process_inputs()
    imgui.new_frame()

    imgui.push_style_var(imgui.STYLE_WINDOW_ROUNDING, 0.0)
    imgui.push_style_color(imgui.COLOR_WINDOW_BACKGROUND, *cfg.color_background)
    imgui.push_style_color(imgui.COLOR_CHECK_MARK, *cfg.color_checkmark)
    imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, *cfg.color_frame_background)
    imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND_ACTIVE,*cfg.color_frame_background)
    imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND_HOVERED, *cfg.color_frame_background)
    imgui.push_style_color(imgui.COLOR_TEXT, *cfg.color_text)
    imgui.push_style_color(imgui.COLOR_POPUP_BACKGROUND, *cfg.color_frame_background_light_shade)
    gui()
    imgui.pop_style_var(1)
    imgui.pop_style_color(7)
    imgui.render()
    impl.render(imgui.get_draw_data())

def exit():
    impl.shutdown()

def gui():
    # Frame 1: drag and drop source
    frame_input()
    frame_buttons()

def frame_input():
    imgui.begin("File input", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)
    imgui.text("Legend: (d) - decompress, (c) - compress, (fc_h) - fctohex, (h_fc) - hextofc")
    imgui.text("Drag and drop files onto this window to add them to the file list.")
    imgui.spacing()
    def tabulate_file(file):
        imgui.push_id(str(file.id)+"fileid")
        file_strings = list()
        file_strings.append(str(file.id))
        file_strings.append(file.title)
        file_strings.append(file.type)
        file_strings.append(file.version)
        # Info text
        for string in file_strings:
            imgui.text(string)
            imgui.next_column()
        # Action checkboxes
        file_id_str = str(file.id)
        action_index = 0
        for action in file.actions:
            _, file.actions[action_index] = imgui.checkbox("##"+str(action_index), action)
            imgui.next_column()
            action_index += 1
        # Interpreter file selection
        _, file.interpreter_i = imgui.combo('##'+"i", file.interpreter_i, cfg.interpreter_files)
        imgui.next_column()
        _, file.interpreter_h = imgui.combo('##'+"h", file.interpreter_h, cfg.interpreter_files)
        imgui.next_column()
        if imgui.button("x", width = 20, height = 20):
            cfg.file_list.remove(file)
        imgui.next_column()
        imgui.separator()
        imgui.pop_id()

    imgui.columns(cfg.table_n_columns)
    imgui.separator()
    for i in range(cfg.table_n_columns):
        imgui.text(cfg.table_headers[i])
        imgui.set_column_width(i, cfg.table_column_width[i])
        imgui.next_column()

    imgui.separator()
    for file in cfg.file_list:
        tabulate_file(file)
    imgui.end()

def frame_buttons():
    imgui.begin("Buttons", False, imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_TITLE_BAR)
    if imgui.button("Process files", width = cfg.button_width, height = cfg.button_height):
        file_handler.process_files()
    imgui.same_line()
    imgui.end()