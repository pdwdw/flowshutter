from machine import Pin, I2C
import ssd1306, time, target

def draw_cam(display):
    # start flowshutter logo
    # first is the "cam"
    display.hline(7,0,18,1)

    display.hline(6,1,6,1)
    display.hline(20,1,6,1)

    display.hline(5,2,6,1)
    display.hline(21,2,6,1)

    display.hline(4,3,6,1)
    display.hline(22,3,6,1)

    display.hline(3,4,7,1)
    display.hline(22,4,7,1)

    display.hline(2,5,8,1)
    display.hline(22,5,8,1)

    display.hline(1,6,10,1)
    display.hline(21,6,10,1)

    display.hline(1,7,30,1)
    display.hline(0,8,32,1)

    display.hline(0,9,4,1)
    display.hline(28,9,4,1)

    display.hline(0,10,3,1)
    display.hline(29,10,3,1)

    display.vline(0,11,17,1)
    display.vline(1,11,17,1)
    display.vline(30,11,17,1)
    display.vline(31,11,17,1)

    display.hline(0,28,3,1)
    display.hline(29,28,3,1)

    display.hline(0,29,4,1)
    display.hline(28,29,4,1)

    display.hline(1,30,30,1)
    display.hline(2,31,28,1)

    display.hline(12,10,7,1)
    display.hline(10,11,11,1)
    
    display.hline(9,12,3,1)
    display.hline(19,12,3,1)

    display.hline(8,13,2,1)
    display.hline(21,13,2,1)

    display.hline(7,14,2,1)
    display.hline(22,14,2,1)

    display.hline(6,15,2,1)
    display.hline(23,15,2,1)

    display.vline(4,18,5,1)
    display.vline(5,16,9,1)
    display.vline(6,16,2,1)
    display.vline(6,23,2,1)

    display.vline(24,16,2,1)
    display.vline(24,23,2,1)
    display.vline(25,16,9,1)
    display.vline(26,18,5,1)

    display.hline(6,25,2,1)
    display.hline(23,25,2,1)
    display.hline(7,26,2,1)
    display.hline(22,26,2,1)

    display.hline(8,27,2,1)
    display.hline(21,27,2,1)

    display.hline(9,28,3,1)
    display.hline(19,28,3,1)
    display.hline(10,29,11,1)

    # now the "status" led
    display.hline(26,11,3,1)
    display.hline(26,15,3,1)
    display.vline(25,12,3,1)
    display.vline(29,12,3,1)

def draw_logo_idle(display):
    
    draw_cam(display)
    # now the "shutter"
    display.hline(13,15,5,1)
    display.hline(13,25,5,1)

    display.vline(9,19,3,1)
    display.vline(21,19,3,1)

    display.line(12,15,9,18,1)
    display.line(9,22,12,25,1)
    display.line(18,15,21,18,1)
    display.line(21,22,18,25,1)
    # end logo

def draw_logo_recording(display):

    draw_cam(display)
    # change the "status"
    display.fill_rect(26,12,3,3,1)
    # now the "shutter"
    display.hline(12,15,7,1)
    display.hline(11,16,9,1)
    display.hline(10,17,11,1)
    display.fill_rect(9,18,13,5,1)
    display.hline(10,23,11,1)
    display.hline(11,24,9,1)
    display.hline(12,25,7,1)

def oled_init():
    _,_,i2c,_,_ = target.init_pins()
    display = ssd1306.SSD1306_I2C(128, 32, i2c)
    display.fill(0)

    draw_logo_idle(display)
    # draw_logo_recording(display)

    display.text('FlowShutter', 40, 0, 1)
    display.text('Powered by', 40, 12, 1)
    display.text('DusKing 0.2', 40, 24, 1)
    display.show()
    return display

def show_arm_info(display):
    display.fill(0)
    draw_logo_recording(display)
    display.text('FlowShutter', 40, 0, 1)
    display.text('FC Armed', 40, 12, 1)
    display.text('Sony recording', 40, 24, 1)
    display.show()

def show_disarm_info(display):
    display.fill(0)
    draw_logo_idle(display)
    display.text('FlowShutter', 40, 0, 1)
    display.text('FC Disarmed', 40, 12, 1)
    display.text('Sony stop', 40, 24, 1)
    display.show()

def show_cam_press_info(display):
    display.fill(0)
    display.text('Cam Pressed', 0, 0, 1)
    display.show()

def show_cam_release_info(display):
    display.fill(0)
    display.text('Cam Released', 0, 0, 1)
    display.show()