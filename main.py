# This is a sample Python script.
import gpiozero


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read_LED_status():
    led = gpiozero.Button(4)
    led.wait_for_active()
    while True:
        print(led.value)

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    read_LED_status()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
