# Audio Narration Instructions

## File Created
- **narration_script.txt**: Complete detailed narration script for WebView integration explanation

## How to Create Audio File

### Option 1: Text-to-Speech (Recommended)
1. Use a TTS service like:
   - **Google Cloud Text-to-Speech** (high quality, natural voices)
   - **Amazon Polly** (AWS, excellent quality)
   - **Microsoft Azure Speech Services** (good quality)
   - **ElevenLabs** (very natural, premium)
   - **Natural Reader** (free option)

2. Copy the content from `narration_script.txt`
3. Generate the audio file
4. Save as `narration.mp3` in the same directory as `presentation_reveal.html`

### Option 2: Professional Voice Recording
1. Hire a voice actor or use a recording service
2. Provide them with `narration_script.txt`
3. Request MP3 format, clear audio quality
4. Save as `narration.mp3`

### Option 3: Free TTS Tools
- **Balabolka** (Windows, free)
- **Natural Reader** (Online, free tier)
- **Google Translate TTS** (for quick testing)

## Script Details
- **Length**: Approximately 8-10 minutes when read at normal pace
- **Style**: Conversational, educational, customer-focused
- **Sections**: 
  1. Introduction
  2. Native Component Data Capture
  3. postMessage Bridge Mechanism
  4. WebView Reception and Real-Time Updates
  5. Bidirectional Communication Flow
  6. Step-by-Step Customer Journey Example
  7. Technical Summary

## Audio Settings Recommendations
- **Format**: MP3
- **Bitrate**: 128 kbps or higher
- **Sample Rate**: 44.1 kHz
- **Channels**: Mono or Stereo
- **Duration**: ~8-10 minutes

## Integration
Once you have `narration.mp3`:
1. Place it in the same directory as `presentation_reveal.html`
2. The audio player in the first slide will automatically detect and play it
3. Users can control playback with the HTML5 audio controls

## Testing
After adding the audio file:
1. Open `presentation_reveal.html` in a browser
2. Navigate to the first slide
3. Click play on the audio controls
4. Verify the audio plays correctly

