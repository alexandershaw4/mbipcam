# Alex's super-light IP cam viewer, by recalling the static jpg with OpenCV
# See mbipc.py Mac manubar launcher that calls this

import urllib
import cv2
import numpy as np
import sys

inp = sys.argv[1:]
inp = int(inp[0])
print(inp)

if inp == 0:
	# This for a static .jpg: call it with a 0:
	# "python view_ipcam.py 0"
	url = 'jpg_snapshot_url'

	while True:
		imgResp = urllib.urlopen(url)
		imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
		img = cv2.imdecode(imgNp,-1)
		cv2.imshow('test',img)
		if ord('q')==cv2.waitKey(10):
			exit(0)

elif inp == 1:
	# This for an rtsp stream, call with 1:
	# "python view_ipcam.py 1"
	 url = 'rtsp_stream_url'

	 cap = cv2.VideoCapture(url)
	 while(True):
	 	ret, frame = cap.read()
	 	cv2.imshow('VIDEO',frame)
	 	if cv2.waitKey(1) & 0xFF == ord('q'):
	 		break

cap.release()
cv2.destroyAllWindows()

