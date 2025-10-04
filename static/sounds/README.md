# Animal Sounds Directory

This directory contains audio files for the Animal Sounds Match game.

## Required Audio Files

To enable real animal sounds in the game, add the following MP3 files to this directory:

1. `lion_roar.mp3` - Lion roaring sound
2. `elephant_trumpet.mp3` - Elephant trumpeting sound
3. `fish_eagle_call.mp3` - African Fish Eagle call
4. `hippo_grunt.mp3` - Hippo grunting sound
5. `hyena_laugh.mp3` - Hyena laughing sound
6. `zebra_bark.mp3` - Zebra barking sound
7. `hornbill_call.mp3` - Hornbill calling sound
8. `baboon_bark.mp3` - Baboon barking sound
9. `leopard_cough.mp3` - Leopard coughing sound
10. `wild_dog_chirp.mp3` - Wild dog chirping sound

## Audio File Requirements

- **Format**: MP3 (recommended for web compatibility)
- **Duration**: 3-10 seconds per sound
- **Quality**: Clear, recognizable animal sounds
- **Volume**: Normalized to consistent levels

## Sources for Animal Sounds

You can obtain royalty-free animal sounds from:

1. **Freesound.org** - Community-driven sound library
2. **Zapsplat.com** - Professional sound effects library
3. **BBC Sound Effects Library** - High-quality nature sounds
4. **YouTube Audio Library** - Free sounds for creators
5. **Pixabay** - Free sound effects

## Fallback Behavior

If audio files are not available, the game will:
- Display a message indicating audio is not available
- Show the sound description instead
- Continue to function normally with text descriptions

## Adding New Animal Sounds

To add new animals to the game:

1. Add the audio file to this directory
2. Update the `animalSounds` array in `/templates/games/animal_sounds.html`
3. Include the new animal in the appropriate options arrays

## File Naming Convention

Use lowercase letters with underscores:
- `animal_name_sound_type.mp3`
- Example: `lion_roar.mp3`, `elephant_trumpet.mp3`

## Copyright Notice

Ensure all audio files are either:
- Royalty-free
- Creative Commons licensed
- Properly attributed if required
- Recorded by you or with permission

Always respect copyright laws when using animal sound recordings.
