import glfw
import OpenGL.GL
import config as cfg
import file_handler

window = None

def start():
    global window
    if not glfw.init():
        print("Could not initialize OpenGL context.")
        exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, OpenGL.GL.GL_TRUE)

    window = glfw.create_window(cfg.window_width, cfg.window_height, cfg.window_name, None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        exit(1)

    glfw.set_drop_callback(window, clb_drop_file)
    return window

def onupdate():
    glfw.poll_events()
    OpenGL.GL.glClearColor(*cfg.clear_color)
    OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT)

def end_frame():
    glfw.swap_buffers(window)

def exit():
    glfw.terminate()


def clb_drop_file(window, paths):
    for path in paths:
        file_handler.process_drop_input(path)