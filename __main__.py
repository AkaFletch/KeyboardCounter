import os
import argparse
import keyboard


class Counter:
    def __init__(self, key, file, prefix):
        count = 0
        if os.path.exists(file):
            with open(file, "r") as deaths:
                text = deaths.read()
                text = text.strip(prefix)
                count = int(text)
        self.deaths = count
        self.file = file
        self.key = key
        self.prefix = prefix

    def call_back(self, event):
        self.deaths = self.deaths + 1
        with open(self.file, "w") as death_file:
            death_file.write(self.prefix + str(self.deaths))
        print("Count at %d" % self.deaths)

    def start(self):
        keyboard.on_release_key(self.key, self.call_back)
        keyboard.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count key presses of a specified key.')
    parser.add_argument(
        'file',
        type=str,
        help='The file to save the count within.'
    )
    parser.add_argument(
        'key',
        type=str,
        help='The key to increment the count.'
    )
    parser.add_argument(
        'prefix',
        type=str,
        help='The prefix to add before the count.'
    )
    args = parser.parse_args()
    Counter(
        args.key,
        args.file,
        args.prefix
    ).start()
