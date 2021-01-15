<h3>Python Automation project</h3>
<b>Grouping image files by day based on image timestamp</b>

<p>The live session of coding this is provided in Youtube channel.</p>

<p>The application should be launched via your terminal by typing following command with arguments:<br><code>python app.py --myimages images</code> where <i>images</i> is the folder name where you are keeping your images which should be grouped based on it's timestamp.</p>

<p>Noting that the timestamp values are extracted from image file name, not from EXIF properties so you should pay attention to timestamp pattern in you image file names. For this project, the pattern of timestamp in image files used: <code>IMG_20201217_220927.jpg</code> equals to <code>IMG_YYYYMMDD_XXXXX.jpg</code>. The main idea is firstly to split the filename between <code>_</code> and extract values from <i>YYYYMMDD</i>.</p>
