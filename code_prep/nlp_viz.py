from bubble_chart import BubbleChart
from nltk.corpus import stopwords
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def pos_tag_color(sentence):
    doc = nlp(sentence)
    displacy.render(doc, style='ent')

def show_wordcloud(data, background_color='white',
                    stopwords=stopwords,
                    max_words=200,
                    max_font_size=40, 
                    scale=3,
                    random_state=1, title=None):
    '''
    Function: Plot the wordcloud
       Input: A bunch of sentences (eg. df['Review'])   
      Output: Wordcloud plot
    '''
    wordcloud = WordCloud(
        background_color=background_color,
        stopwords=stop_words,
        max_words=max_words,
        max_font_size=max_font_size, 
        scale=scale,
        random_state=random_state # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()

def bubble_chart(bigram_df, top_n, bubble_spacing=0.001, COLOR=sns.color_palette("Paired").as_hex()):
    '''
    Function: Plot the bubble chart for Bigram
       Input: Bigram dataframe with frequence,
              rename the cols, columns=['bigram', 'freq']
      Output: Bubble chart plot
    '''
    bigram_df = bigram_df[:top_n].sample(frac=1).reset_index(drop=True)
    if type(bigram_df['bigram'][0]) == tuple:
        bigram_df['bigram'] = bigram_df['bigram'].apply(lambda x:' '.join(x))
    bigram_df['Color'] = np.random.choice(COLOR, top_n)
    bubble_chart = BubbleChart(area=bigram_df['freq'],
                           bubble_spacing=bubble_spacing)
    bubble_chart.collapse()
    fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
    fig.set_size_inches(9, 13, forward=True)
    bubble_chart.plot(ax, bigram_df['bigram'], bigram_df['Color'])
    ax.axis("off")
    ax.relim()
    ax.autoscale_view()
    plt.show()



