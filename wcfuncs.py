#
# WordCloud functions
#

# Packages
from wordcloud import WordCloud, STOPWORDS
import re
import matplotlib.pyplot as plt
import os


def replace_strings(in_text, replacements):
    '''
    Replace key strings by value strings in text.
    
    PARAMETERS:
      - in_text: text before string replacement
      - replacements: dictionary containing keys --> values to be replaced
      
    RETURNS:
      - out_text: text after string replacement
      
    '''
    
    # Function taken from this post:
    # https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
    
    
    # Escape
    rep = dict((re.escape(k), v) for k, v in replacements.iteritems())
    
    # Compile all keys into single string, separated by |
    pattern = re.compile("|".join(rep.keys()))
        
    # Substitute
    out_text = pattern.sub(lambda m: rep[re.escape(m.group(0))], in_text)
    
    return out_text




def make_wordcloud(
    text, 
    outfile,
    custom_sw = None,
    reduction = None,
    figure_size = (20,10),
    display = False):

    """    Generate a square wordcloud.
    
    """
    
    # Ensure output directory exists. If not, create.
    directory = '/'.join(outfile.split('/')[:-1]) # split by '/'; remove last element (file); join by '/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Join default and custom stopwords
    if custom_sw is not None:
        sw = STOPWORDS.union(custom_sw)

    # Reduce 
    if reduction is not None:
        text = replace_strings(text, reduction)

    # Create wordcloud
    wordcloud = WordCloud(
        max_font_size=60, 
        stopwords=sw,
        background_color='black'
        ).generate(text)

    plt.figure(figsize=figure_size)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(outfile, bbox_inches='tight');
    
    if display:
        plt.show()
        
    pass
