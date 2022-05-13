import glfw
import OpenGL.GL
import config as cfg
import gui_implementation as gui
import window

def glfw_init():
    if not glfw.init():
        print("Could not initialize OpenGL context.")
        exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, OpenGL.GL.GL_TRUE)

    appwindow = glfw.create_window(cfg.window_width, cfg.window_height, cfg.window_name, None, None)
    glfw.make_context_current(appwindow)

    if not appwindow:
        glfw.terminate()
        print("Could not initialize Window")
        exit(1)

    return appwindow


if __name__ == "__main__":
    application_window = window.start()
    gui.start(application_window)
    while not glfw.window_should_close(application_window):

        window.onupdate()
        gui.onupdate()
        window.end_frame()

    gui.exit()
    window.exit()
