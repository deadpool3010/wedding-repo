# Krishna & Pramey — wedding invitation site

Files
- `wedding.json` – all text, dates, venues, map links and events, keyed by screen (opening, hero, countdown, events, blessings, thankYou).
- `template.html` – layout, styles, animations.
- `index.html` – the built page (template + JSON baked in, so it also opens by double-click).
- `build.py` – run `python3 build.py` after editing the JSON to refresh the baked-in copy.

When served from a web server, the page reads `wedding.json` live; opened as a file, it uses the baked-in copy.

Images: set `backgroundImage` on `opening`, `hero` or `thankYou` (e.g. `"assets/temple.png"`) to replace the drawn scenery with your own art.
Countdown target: `screens.countdown.target` (ISO time with +05:30).

Music:
- Built-in zero-latency Web Audio Synthesizer playing serene Indian Classical wedding music (Shehnai melody in Raag Yaman, Tanpura drone, and sacred Temple Chimes).
- Autoplays gracefully when the user taps "Tap to open" on the gate cover (meeting modern browser user-gesture requirements).
- Floating gold music toggle button in the bottom-right corner with dancing sound waves and gentle pulsing animations to pause or play at any time.
- Optional custom song: set `"src": "assets/your-music.mp3"` under `"music"` in `wedding.json` to play an MP3 instead.
