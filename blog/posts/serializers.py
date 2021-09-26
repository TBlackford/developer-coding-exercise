from rest_framework import serializers

stop_words = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]


class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.CharField()
    title = serializers.CharField()
    tags = serializers.SerializerMethodField('get_tags')

    def get_tags(self, text, num):
        """
        Get all the tags used in the text and return in a list.
        NB: this could probably be a single line but that would not be very human-readable so I split it up
        :param text: the text of the blog post to parse
        :param num: the number of the top most used stopwords to return
        :return: list of the stopwords
        """

        # Filter out non-stopwords
        stopwords_in_text = [stopword for stopword in ''.join(text).split(" ") if stopword in stop_words]

        # Count the instances of the stopwords
        counted_stopwords = dict((word, stopwords_in_text.count(word)) for word in set(stopwords_in_text))

        # Sort these instances then remove all but the num specified
        sorted_words = [word for word in
                        sorted(counted_stopwords.items(), key=lambda item: item[1], reverse=True)[:num]]

        # Previous line in a dict with (word: count) so just get the key
        return [key for (key, value) in sorted_words]

    def to_representation(self, data):
        """
        Override how the json object will look
        :param data: the text from the file
        :return: the formatted json
        """
        title = data[1].replace('Title: ', '').replace('\n', '')
        author = data[2].replace('Author: ', '').replace('\n', '')

        print(data[5:])

        return {
            'post': {
                'content': ''.join(data[5:]),  # Strip out the meta stuff
                # In the future, I would like to not do this and pull the data from a DB
                'title': title,
                'author': author,
                'tags': self.get_tags(data, 5)
            }
        }
