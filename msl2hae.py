import subprocess

def get_ellipsoidal_height(lat, lon, msl_height):
    GepodEval_output = subprocess.check_output(f"echo {lat} {lon} {msl_height} | GeoidEval -n egm2008-1 --msltohae", shell=True)
    ellipsoidal_height = float(GepodEval_output.decode("utf-8").split()[-1])
    return ellipsoidal_height

lat = 22.3207
lon = 113.8805	
msl_height = 34.96
ellipsoidal_height = get_ellipsoidal_height(lat, lon, msl_height)
print(ellipsoidal_height)