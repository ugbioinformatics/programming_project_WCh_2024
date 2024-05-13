# programming_project_WCh_2024
          Instructions to allow Firefox to open local HTML files that use Jmol

(1) Open Firefox. Go to the URL about:config (type this in the URL bar at the top of the Firefox window.)

(2) Set the switch "security.fileuri.strict_origin_policy" to "false" - this can be done by clicking on the switch.

Instalacja
virtualne środowisko
<pre>
python3 -m venv env
source env/bin/activate.csh
pip install -r requirements.txt
ln -s /usr/lib/python3/dist-packages/openbabel $VIRTUAL_ENV/lib/python*/site-packages
</pre>

<pre>
git clone git@github.com:ugbioinformatics/programming_project_WCh_2024.git
cd programming_project_WCh_2024          
pip install -r requirements.txt
cd abecadlo/
python3 manage.py makemigrations blog
python3 manage.py migrate
python3 manage.py runserver
</pre>


