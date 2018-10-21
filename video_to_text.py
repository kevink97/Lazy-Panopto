#This code was taken from and belongs to

import argparse

from google.cloud import videointelligence_v1p1beta1 as videointelligence


# [START video_speech_transcription_gcs_beta]
def speech_transcription(input_uri):
    """Transcribe speech from a video stored on GCS."""
    video_client = videointelligence.VideoIntelligenceServiceClient()

    features = [videointelligence.enums.Feature.SPEECH_TRANSCRIPTION]

    config = videointelligence.types.SpeechTranscriptionConfig(
        language_code='en-US',
        enable_automatic_punctuation=True)
    video_context = videointelligence.types.VideoContext(
        speech_transcription_config=config)

    operation = video_client.annotate_video(
        input_uri, features=features,
        video_context=video_context)

    print('\nProcessing video for speech transcription.')

    result = operation.result(timeout=300)

    # There is only one annotation_result since only
    # one video is processed.
    annotation_results = result.annotation_results[0]
    speech_transcription = annotation_results.speech_transcriptions[0]
    alternative = speech_transcription.alternatives[0]

    print('Transcript: {}'.format(alternative.transcript))
    print('Confidence: {}\n'.format(alternative.confidence))

    print('Word level information:')
    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time
        print('\t{}s - {}s: {}'.format(
            start_time.seconds + start_time.nanos * 1e-9,
            end_time.seconds + end_time.nanos * 1e-9,
            word))
# [END video_speech_transcription_gcs_beta]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    speech_transcription_parser = subparsers.add_parser(
        'transcription', help=speech_transcription.__doc__)
    speech_transcription_parser.add_argument('gcs_uri')

    args = parser.parse_args()

    if args.command == 'transcription':
        speech_transcription(args.gcs_uri)