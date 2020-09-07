__version__ = "0.0.12"
import matplotlib as mpl, pkgutil
from fastai.vision.all import *
from pandas.api.types import CategoricalDtype
from scipy.cluster import hierarchy as hc
from io import StringIO, BytesIO

try: from ipywidgets import widgets
except ModuleNotFoundError: warn("Missing `ipywidgets` - please install it")
try: import sentencepiece
except ModuleNotFoundError: warn("Missing `sentencepiece` - please run `pip install 'sentencepiece<0.1.90'`")
try:
    from azure.cognitiveservices.search.imagesearch import ImageSearchClient as api
    from msrest.authentication import CognitiveServicesCredentials as auth
except ModuleNotFoundError:
    warn("Missing Azure SDK - please run `pip install azure-cognitiveservices-search-imagesearch`")
try: from nbdev.showdoc import *
except ModuleNotFoundError: warn("Missing `nbdev` - please install it")
try:
    import graphviz
    from sklearn.tree import export_graphviz
except ModuleNotFoundError: warn("Missing `graphviz` - please run `conda install fastbook`")

mpl.rcParams['savefig.dpi']= 200
mpl.rcParams['font.size']=12

set_seed(42)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
pd.set_option('display.max_columns',999)
np.set_printoptions(linewidth=200)
torch.set_printoptions(linewidth=200)

def setup_colab():
    "Sets up Colab. First run `!pip install -Uqq fastbook` in a cell"
    assert IN_COLAB, "You do not appear to be running in Colab"
    global gdrive
    gdrive = Path('/content/gdrive/My Drive')
    from google.colab import drive
    if not gdrive.exists(): drive.mount(str(gdrive.parent))

def setup_book():
    if IN_COLAB: return setup_colab()

def gv(s): return graphviz.Source('digraph G{ rankdir="LR"' + s + '; }')

def get_image_files_sorted(path, recurse=True, folders=None):
    return get_image_files(path, recurse, folders).sorted()

def search_images_bing(key, term, min_sz=128):
    client = api('https://api.cognitive.microsoft.com', auth(key))
    return L(client.images.search(query=term, count=150, min_height=min_sz, min_width=min_sz).value)

def plot_function(f, tx=None, ty=None, title=None, min=-2, max=2, figsize=(6,4)):
    x = torch.linspace(min,max)
    fig,ax = plt.subplots(figsize=figsize)
    ax.plot(x,f(x))
    if tx is not None: ax.set_xlabel(tx)
    if ty is not None: ax.set_ylabel(ty)
    if title is not None: ax.set_title(title)

def draw_tree(t, df, size=10, ratio=0.6, precision=0, **kwargs):
    s=export_graphviz(t, out_file=None, feature_names=df.columns, filled=True, rounded=True,
                      special_characters=True, rotate=False, precision=precision, **kwargs)
    return graphviz.Source(re.sub('Tree {', f'Tree {{ size={size}; ratio={ratio}', s))

def cluster_columns(df, figsize=(10,6), font_size=12):
    corr = np.round(scipy.stats.spearmanr(df).correlation, 4)
    corr_condensed = hc.distance.squareform(1-corr)
    z = hc.linkage(corr_condensed, method='average')
    fig = plt.figure(figsize=figsize)
    hc.dendrogram(z, labels=df.columns, orientation='left', leaf_font_size=font_size)
    plt.show()

def image_cat (): return BytesIO(pkgutil.get_data('fastbook', 'images/cat.jpg'))
def image_bear(): return BytesIO(pkgutil.get_data('fastbook', 'images/grizzly.jpg'))

