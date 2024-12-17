from sense_emu import SenseHat
import time

# Khởi tạo Sense HAT (mô phỏng)
sense = SenseHat()

# Tên hiển thị trên LED Matrix
name = "Duc"
color = (255, 0, 0)  # Màu đỏ

def display_name_on_led(name, color):
    """
    Hiển thị tên trên LED Matrix.
    """
    sense.show_message(name, text_colour=color, scroll_speed=0.1)

while True:
    try:
        # Đọc nhiệt độ và độ ẩm
        temp = sense.get_temperature()
        humidity = sense.get_humidity()

        # Hiển thị nhiệt độ và độ ẩm trên console
        print(f"Nhiệt độ: {temp:.2f}°C, Độ ẩm: {humidity:.2f}%")

        # Lấy trạng thái joystick
        joystick_events = sense.stick.get_events()

        # Hiển thị trạng thái joystick trên console
        for event in joystick_events:
            print(f"Joystick Event: Direction={event.direction}, Action={event.action}")

        # Hiển thị tên trên LED Matrix
        display_name_on_led(name, color)

        # Tạm dừng 2 giây trước khi lặp lại
        time.sleep(2)

    except KeyboardInterrupt:
        # Dừng chương trình khi nhấn Ctrl+C
        print("Dừng chương trình.")
        sense.clear()
        break