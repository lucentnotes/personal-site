# Licensed film-score audition

A separate audition using recorded compositions by Scott Buckley. Main film remains unchanged.

Daily-life cue: Reverie, source 0–97.2 seconds. Ballroom/ending cue: Moonlight, source 1.8–38.24 seconds; removes original opening silence. Neither is looped during the timed film. The final notebook wait may repeat only the final short musical region while waiting for the viewer, followed by the existing closure fade.

Original recorded tempo is preserved at new 1x. The 191-second logical timeline corresponds to 152.8 seconds of default viewing. Exiting shop reaches silence at logical 121.5; music returns at logical 145.45. This is a proposed new musical attack at the existing action cue, not the previously approved original piano recording.

CC BY 4.0 and authorship confirmed from each composer's official track page and usage page. Full track attribution, source links, license link and edit disclosure appear both on the audition landing page and in the in-film Music credits dialog. No separate music-only player or complete original recordings are offered. Source record contains hashes of the downloaded recordings and identifies their public distribution mirror.

Rebuild: supply reverie.mp3 and moonlight.mp3 in a directory and run tools/render_licensed_score.py /path/to/directory then tools/build_licensed_score.py. Requirements: NumPy, FFmpeg. Runtime is derived from the isolated music-study clock implementation.
