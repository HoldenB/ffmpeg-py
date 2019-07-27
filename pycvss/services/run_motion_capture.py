import pycvss.ffmpeg.fdcm as fdcm
import pycvss.sample_files as sample_files


###############################################################################
if __name__ == "__main__":
    # Testing the FDCM detector
    fdcm_detector = fdcm.Fdcm()
    fdcm_detector.input_file = sample_files.SAMPLE_VIDEO_HD_MOV
    fdcm_detector.process()
