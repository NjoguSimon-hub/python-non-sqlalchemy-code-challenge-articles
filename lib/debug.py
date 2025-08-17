#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    
    # Create some sample instances for testing
    author1 = Author("Carry Bradshaw")
    author2 = Author("Nathaniel Hawthorne")
    magazine1 = Magazine("Vogue", "Fashion")
    magazine2 = Magazine("AD", "Architecture")
    
    article1 = Article(author1, magazine1, "How to wear a tutu with style")
    article2 = author1.add_article(magazine2, "2023 Eccentric Design Trends")
    
    print(f"Author1 articles: {len(author1.articles())}")
    print(f"Magazine1 articles: {len(magazine1.articles())}")
    print(f"Author1 topic areas: {author1.topic_areas()}")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
