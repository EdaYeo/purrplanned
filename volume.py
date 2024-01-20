import sounddevice as sd
import numpy as np
import threading
import time

def get_microphone_volume(duration=5):
    volume_data = []

    def callback(indata, frames, time, status):
        if status:
            print(f"Error in audio input: {status}")
        volume_data.extend(np.abs(indata.flatten()))

    with sd.InputStream(callback=callback):
        sd.sleep(duration * 1000)

    return np.mean(volume_data)

def show_volume_indicator(duration=1):
    start_time = time.time()
    while time.time() - start_time < duration:
        volume = get_microphone_volume()
        show_single_volume(volume)
        time.sleep(1)  # Adjust the sleep duration as needed for responsiveness

def show_single_volume(volume):
    volume_int = int(volume * 500000)  # Convert volume to an integer
    print(f"Microphone Volume: {volume_int}")

def main():
    duration = 1  # Duration for microphone input
    microphone_thread = threading.Thread(target=lambda: show_volume_indicator(duration))
    microphone_thread.start()
    microphone_thread.join()

if __name__ == "__main__":
    main()
