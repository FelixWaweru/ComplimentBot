text = ["❤️", "♥️", "💗", "💓", "💕", "💖", "💞 " "💘", "💛", "💙", "💜", "💚", "💝", "💌", "🌝", "🌞", "☀️"]
for i, line in enumerate(text):
    if "\xe2" in line:
        print (i), repr(line)