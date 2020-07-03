import os, random, glob
import pandas as pd

path_folder = os.path.dirname(os.path.dirname(os.path.abspath('imagetest')))
path = os.path.join(path_folder, 'employee/static/assets/student/image/imagetest')
files = os.listdir(path)


def parse_filepath(filepath):
    try:
        path, filename = os.path.split(filepath)
        label, _ = filename.split(".")
        return label
    except Exception as e:
        print('error to parse %s. %s' % (filepath, e))
        return None, None


files = glob.glob(os.path.join(path, "*.png"))[:10]
attributes = list(map(parse_filepath, files))

df = pd.DataFrame(attributes)
df['file'] = files
df.columns = ['label', 'file']
label_file = set(zip(df['label'].tolist(), df['file'].tolist()))

