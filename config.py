import os
window_width = 960
window_height = 540
window_name = "Anno 1800 - FileDBReader GUI"
clear_color = (0.0, 0.0, 0.0, 1.0)
color_background = (167/255, 208/255, 228/255)
color_frame_background = (227/255, 231/255, 203/255)
color_frame_background_light_shade = (247/255, 241/255, 213/255)
color_checkmark = (0.2, 0.2, 0.22)
color_text = (0.1, 0.1, 0.1)
## File input frame
table_headers = ["ID", "File path", "Type", "Version", "d", "c", "fc_h", "h_fc", "interpret", "toHex", " x"]
table_n_columns = len(table_headers)
table_column_width = [50, 280, 50, 65, 50, 50, 50, 50, 135, 135, 50]

interpreter_files = os.listdir("FileDB/FileFormats")
interpreter_files.insert(0, "-")
# Runtime:
file_list = list()

button_width = 130
button_height = 37