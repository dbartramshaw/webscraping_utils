#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Website Feature Extraction
"""


import json
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# import sys
# sys.path.insert(0, "/Users/bartramshawd/pyner-master")
# import ner
# tagger = ner.HttpNER(host='localhost', port=8080)
# tagger.get_entities("University of California is located in California, United States")

from unidecode import unidecode
def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))


def clean_text_iter(strg):
    import re
    from nltk.corpus import stopwords
    """
    Clean string.
        - replaces Unicode with appropriate letter
        - removes website patterns (retain names)
        - Removes all non alphabetical characters and retains numbers
        - converts to lower case
        - removes stopwords.words('english') from NLTK library
    ----------
    Parameters
    ----------
    strg : single string
    """
    s = unidecode(strg)
    patterns = ['.co.uk','.com','www.','.net','.org']
    patterns = ','.join(patterns)
    s = re.sub('\\b'+patterns+'\\b', ' ', s)
    s = re.sub(" +"," ", s)
    #s = re.sub("[^a-zA-Z,\s]", '', strg)
    s = re.sub("[^a-zA-Z0-9]"," ", s)
    s = s.lower()
    sw = stopwords.words('english')
    s = ' '.join([word for word in s.split() if word not in sw])
    return s



remove_format_indicators=['share','events','webcast','event','webinar','forum','microsoft','learn','read']
def remove_selected_words(s,remove_words):
    #remove_words = ['january','february','march','april','may','june','july','august','september','october','november','december']
    s = ' '.join([word for word in s.split() if word not in remove_words])
    return s



# REFORMAT TO DICT
def format_data(project_path,
                remove_words=[]
                ):
    global page_dict,urls,text,clean_text,layers,clean_text_dict

    page_data = []
    for line in open(project_path+'data/html_dict.json', 'r'):
        page_data.append(json.loads(line))
    urls = [page_data[x]['url'] for x in range(0,len(page_data))]
    links = [page_data[x]['links'] for x in range(0,len(page_data))]
    text = [page_data[x]['text'] for x in range(0,len(page_data))]
    meta = [{k:v for k, v in page_data[x].items() if k!='url'} for x in range(0,len(page_data))]
    page_dict = dict(zip(urls,meta))
    print('--------------------------')
    print('COMPLETE: Data loaded')

    layers = pd.read_csv(project_path+'sitemap_vis/'+'sitemap_all_layers.csv')
    layers.dropna(how='all',axis=1,inplace=True)
    layers.fillna('',inplace=True)
    print('COMPLETE: Sitemap layers loaded')

    with open(project_path+'data/'+project_title+'website_data.json', 'w') as f:
        json.dump(page_dict, f)
    print('COMPLETE: Data Saved')

    clean_text = [clean_text_iter(t) for t in text]
    clean_text_dict = dict(zip(urls,clean_text))
    print('COMPLETE: Text Cleaned')
    print('--------------------------')


#######################
# LOAD & FORMAT DATA
#######################
format_data(project_path)
#Check one value
page_dict[page_dict.keys()[0]]



#######################
# AUTO INDUSTRY FINDER
#######################

#!!! INPUTS
# define what layer shows industries
industry_sitemap_layer  = 2
# define the exact name of the indutry from the sitemap
industry_name = 'industries'

# # MANUAL
# # Find unique industries
# unique_industries = layers[layers[str(industry_sitemap_layer-1)]==industry_name][str(industry_sitemap_layer)].unique()
# unique_industries = [x for x in unique_industries if len(x) > 1]
#
# # Does url have industry?
# industry_data_idx = layers[str(industry_sitemap_layer-1)]==industry_name
# layers['industry_tag'] = layers[str(industry_sitemap_layer-1)]==industry_name
# layers['industry_name'] = layers[str(industry_sitemap_layer)].apply(lambda x: x if x in unique_industries else 'None')
# indutries_url_dict = dict(zip(layers['url'],layers['industry_name'] ))


class findAdd_sitemapFeat(object):
        """
            ----------------------------------------
            FIND AND ADD FEATURES FROM SITEMAP
            ----------------------------------------
            Uses the sitemap structure to find and segment urls
            Examples of this could be tagging each url by industry
            Allows you to add multiple features to then further process

            Parameters:
    		-----------
    		sitemap_df      : pd.DataFrame
            feat_layer      : the number layer that indicates your feature i.e industry
            feat_name_layer : the number layer that names the feature i.e industry_name
            feat_str_nam    : the value of the str that indicates your feature i.e industry

    		Returns:
    		-----------
    		self: update of the class attributes

            self.sitemap_df     - updated imput with added columns
            self.feat_url_dict  - url to feat lookup
            self.unique_feats   - number of distinct feature values

        """

        def __init__(self,
                     sitemap_df,
                     feat_layer=1,
                     feat_name_layer=2,
                     feat_str_name='industries'):
            print('-------------------------------')
            feat_layer=str(feat_layer)
            feat_name_layer=str(feat_name_layer)

            #Find unique industries
            self.unique_feats = sitemap_df[sitemap_df[feat_layer]==feat_str_name][feat_name_layer].unique()
            self.unique_feats = [x for x in self.unique_feats if len(x) > 1]
            print(str(len(self.unique_feats))+' different '+feat_str_name+' found')

            # Does url have industry?
            industry_data_idx = sitemap_df[feat_layer]==feat_str_name

            sitemap_df[feat_str_name+'_tag_yn'] = sitemap_df[feat_layer]==feat_str_name
            sitemap_df[feat_str_name+'_name'] = sitemap_df[feat_name_layer].apply(lambda x: x if x in self.unique_feats else 'None')
            self.sitemap_df=sitemap_df

            # industry dict
            self.feat_url_dict = dict(zip(sitemap_df['url'],sitemap_df[feat_str_name+'_name']))
            print('Dict lookup complete')
            print('------------------------------')


# def findAdd_industry(sitemap_df,
#                      industry_layer=1,
#                      industry_name_layer=2,
#                      industry_str='industries'
#                      ):
#         global indutries_url_dict,unique_industries
#
#         print('-------------------------------')
#         industry_layer=str(industry_layer)
#         industry_name_layer=str(industry_name_layer)
#
#         #Find unique industries
#         unique_industries = sitemap_df[sitemap_df[industry_layer]==industry_str][str(industry_name_layer)].unique()
#         unique_industries = [x for x in unique_industries if len(x) > 1]
#         print(str(len(unique_industries))+' different '+industry_str+' found')
#
#         # Does url have industry?
#         industry_data_idx = sitemap_df[industry_layer]==industry_str
#
#         sitemap_df[industry_str+'_tag_yn'] = sitemap_df[industry_layer]==industry_str
#         sitemap_df[industry_str+'_name'] = sitemap_df[industry_name_layer].apply(lambda x: x if x in unique_industries else 'None')
#
#         # industry dict
#         indutries_url_dict = dict(zip(sitemap_df['url'],sitemap_df[industry_str+'_name']))
#         print('Dict lookup complete')
#         print('------------------------------')
#
#         return sitemap_df



industry_feature = findAdd_sitemapFeat(layers,
                                       feat_layer=industry_sitemap_layer-1,
                                       feat_name_layer=industry_sitemap_layer,
                                       feat_str_name='industries')

print industry_feature.__doc__
industry_feature.unique_feats

['natural-resources',
 'aerospace-defense',
 'architecture-engineering-construction',
 'high-tech',
 'life-sciences',
 'transportation-mobility',
 'consumer-goods-retail',
 'consumer-packaged-goods-retail',
 'financial-and-business-services',
 'marine-offshore',
 'industrial-equipment',
 'energy-process-utilities']


#######################
# TEXT FEATURES
#######################

class word_features_sim(object):
        """
            ----------------------------------------
            WORD FEATURE & SIMILARITY GENERATION
            ----------------------------------------
            Features are created on eitehr TFIDF or FREQ levels
            Outputs are dataframe formatted for visualisation & Dictionary form for processing

            Parameters:
    		-----------
    		input_text     :  np.array. text (Documents)
            vec_type       : 'tfidf' or 'freq'

    		Returns:
    		-----------
    		self: update of the class attributes
            self.word_features (tfidf matrix)
            self.feature_names
            self.top_words_per_doc
            self.top_similar_docs

        """

        def __init__(self
                    ,input_text
                    ,vec_type='tfidf'
                    ,n_top_words=20
                    ,n_similar_docs=20
                    ,sublinear_tf=False
                    ,ngram_range=(1,1)
                    ,norm=None
                    ,max_features=None):

            if vec_type=='tfidf':
                from sklearn.feature_extraction.text import TfidfVectorizer
                vectorizer = TfidfVectorizer(analyzer='word',stop_words='english',ngram_range=ngram_range,max_features=max_features) #sublinear_tf=True,

            if vec_type=='freq':
                from sklearn.feature_extraction.text import CountVectorizer
                vectorizer = CountVectorizer(analyzer='word',stop_words='english',ngram_range=ngram_range,max_features=max_features) #sublinear_tf=True,

            self.word_features = vectorizer.fit_transform(input_text)
            self.feature_names = vectorizer.get_feature_names()
            print('-----------------------------------------')
            print('COMPLETE: '+vec_type+' Word Features Generated')

            # Store all word that appear in each doc and TFIDF score
            _df = pd.DataFrame({'doc_index':self.word_features.nonzero()[0], 'doc_matrix_indices':self.word_features.nonzero()[1], vec_type:self.word_features.data})
            _df['phrase']=[self.feature_names[x] for x in _df.doc_matrix_indices]
            _df = _df.sort_values(['doc_index',vec_type],ascending=[1,0])
            _df['rank']=_df.groupby('doc_index')[vec_type].rank(ascending=False)


            # Store top words
            self.top_words_per_doc = _df[_df['rank']<=n_top_words]
            self.top_words_per_doc = self.top_words_per_doc.groupby('doc_index').agg({'phrase':lambda x:', '.join(x)}).reset_index()
            print('COMPLETE: Top words generated')

            # Top similar between each doc
            cosine_df = pd.DataFrame((self.word_features * self.word_features.T).A)
            cs_df_reshaped = pd.DataFrame(cosine_df.stack()).reset_index()
            cs_df_reshaped.columns=[['doc_index','compared_doc_index','cosine_similarity']]
            cs_df_reshaped['rank']=cs_df_reshaped.groupby('doc_index')['cosine_similarity'].rank(ascending=False)
            self.top_similar_docs = cs_df_reshaped[cs_df_reshaped['rank']<=n_similar_docs].sort_values(['doc_index','rank'],ascending=[1,1])
            print('COMPLETE: Similarity computed')
            print('-----------------------------------------')
