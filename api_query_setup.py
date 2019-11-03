#!/usr/bin/env python

"""
Module for setting up a query to be used with the Thompson Reuters API

Author: Tilia Ellendorff
"""

class QuerySetup(object):
    
    def __init__(self, authtoken, num_years=1, languages=['en'], geography=None):
        '''
        Object for setting up a query.
        :: num_years - past number of years to consider (default is one year)
        :: languages - list languages to consider (default is English)
        :: geography - list of countries to consider (by default all countries are included)
        '''
        
        self.token = authtoken
        self.num_years = num_years
        self.languages = languages
        self.geography = geography
        self.geography_query = self._format_geography()
        self.daterange_query = self._format_daterange()
        self.language_query = self._format_languages()
        self.mediatype_query = 'T'
        
        # terms to be search in fulltext
        self.query_terms = [
            'human trafficking',
            'slavery',
            'child labour',
            'child labor',
            'forced labor',
            'force labour',
            'debt boundage']
        
        self.text_query = self._format_text_query()
        
    def _format_daterange(self):
        
        current_date = datetime.today().date().strftime("%Y.%m.%d")
        past_datetime = datetime.today() - timedelta(days=self.num_years*365)
        past_date = past_datetime.strftime("%Y.%m.%d")
        
        return f'{past_date}-{current_date}'
    
    def _format_languages(self):
        langs = [f'language={lang}' for lang in self.languages]
        return '&'.join(langs)
    
    def _format_geography(self):
        '''Format geography query as follows: 'geography=USA&geography=CAN'''
        if self.geography is not None:
            geos = [f'geography={geo}' for geo in self.geography] 
            return '&'.join(geos)    
    
    def _format_text_query(self):
        qts = [f'"{qt}"' for qt in self.query_terms]
        qt_string = ' OR '.join(qts)
        return f'main:({qt_string})'        
            
    def query_url(self):
        #url = f'http://rmb.reuters.com/rmd/rest/json/search?q={search_query}&mediaType=T&token={authToken}&format=json' 
        url = f'http://rmb.reuters.com/rmd/rest/json/search?q={self.text_query}&mediaType={self.mediatype_query}&dateRange={self.daterange_query}&{self.language_query}&{self.geography_query}&limit=10000&token={self.token}'
        return url
        
        