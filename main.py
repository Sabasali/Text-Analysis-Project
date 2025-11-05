"""
Text Analysis Project - Drake vs Taylor Swift
Parts of this code were developed with assistance from ChatGPT.
"""

import wikipediaapi
import string
import math

# -----------------------------
# STEP 1: FETCH TEXT FROM WIKIPEDIA
# -----------------------------
def fetch_wikipedia_text(title):
    """
    Fetches plain-text content of a Wikipedia page using a polite user agent.
    """
    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="TextAnalysisProject/1.0 (for Babson College software class)"
    )

    page = wiki.page(title)
    if not page.exists():
        print(f"[ERROR] Page '{title}' does NOT exist!")
        return ""
    return page.text


# -----------------------------
# STEP 2: TEXT CLEANING
# -----------------------------
def clean_text(text):
    """
    Lowercase, remove punctuation and numbers, and split into words.
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = "".join([char for char in text if not char.isdigit()])
    words = text.split()
    return words


# -----------------------------
# STEP 3: REMOVE STOPWORDS
# -----------------------------
STOPWORDS = {
    "the", "and", "a", "an", "of", "to", "in", "is", "it", "that", "this", "for", "on", "with", "as",
    "by", "at", "from", "or", "be", "are", "was", "were", "but", "not", "have", "has", "had", "they",
    "their", "them", "you", "your", "i", "he", "she", "we", "us", "our", "his", "her", "its", "which",
    "who", "whom", "what", "when", "where", "why", "how", "so", "if", "than", "then", "there", "here",
    "can", "could", "would", "should", "do", "does", "did", "been", "will", "shall", "also"
}

def remove_stopwords(words):
    """
    Remove common stopwords from a list of words.
    """
    return [w for w in words if w not in STOPWORDS]


# -----------------------------
# STEP 4: WORD FREQUENCY + STATS
# -----------------------------
def word_frequencies(words):
    """
    Create a dictionary counting each word's frequency.
    """
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def summary_stats(words):
    """
    Return total words, unique words, and average word length.
    """
    total = len(words)
    unique = len(set(words))
    if total == 0:
        avg_len = 0
    else:
        avg_len = sum(len(w) for w in words) / total
    return total, unique, avg_len


# -----------------------------
# STEP 5: DISPLAY TOP WORDS
# -----------------------------
def print_top_words(freq_dict, title, n=15):
    """
    Print the top N most frequent words.
    """
    print(f"\nTop {n} words for {title}:")
    print("-" * 40)
    for word, count in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:n]:
        print(f"{word:>15} : {count}")


# -----------------------------
# STEP 6: ASCII BAR CHART (VISUALIZATION)
# -----------------------------
def ascii_bar_chart(freq_dict, title, n=15):
    """
    Print a simple ASCII bar chart of the top N words.
    """
    top_items = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:n]
    if not top_items:
        print(f"\n[No data for {title}]")
        return

    max_count = top_items[0][1]
    if max_count == 0:
        print(f"\n[No data for {title}]")
        return

    scale = max_count / 40  # scale bars to ~40 characters

    print(f"\nASCII bar chart for {title}:")
    print("-" * 40)
    for word, count in top_items:
        bar_len = max(1, int(count / scale))
        bar = "#" * bar_len
        print(f"{word:>15} | {bar} ({count})")


# -----------------------------
# STEP 7: COSINE SIMILARITY (TEXT SIMILARITY TECHNIQUE)
# -----------------------------
def cosine_similarity(freq1, freq2):
    """
    Compute cosine similarity between two word-frequency dictionaries.
    """
    all_words = set(freq1.keys()) | set(freq2.keys())
    dot = 0
    norm1 = 0
    norm2 = 0

    for w in all_words:
        v1 = freq1.get(w, 0)
        v2 = freq2.get(w, 0)
        dot += v1 * v2
        norm1 += v1 * v1
        norm2 += v2 * v2

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot / (math.sqrt(norm1) * math.sqrt(norm2))


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    print(">>> STARTING TEXT ANALYSIS <<<")

    # Step 1: Fetch text
    drake_text = fetch_wikipedia_text("Drake (musician)")
    taylor_text = fetch_wikipedia_text("Taylor Swift")

    # Step 2: Clean text
    drake_words = clean_text(drake_text)
    taylor_words = clean_text(taylor_text)

    # Step 3: Remove stopwords
    drake_filtered = remove_stopwords(drake_words)
    taylor_filtered = remove_stopwords(taylor_words)

    # Step 4: Frequency + stats
    drake_freq = word_frequencies(drake_filtered)
    taylor_freq = word_frequencies(taylor_filtered)

    d_total, d_unique, d_avg_len = summary_stats(drake_filtered)
    t_total, t_unique, t_avg_len = summary_stats(taylor_filtered)

    print("\nSummary statistics:")
    print("-------------------")
    print(f"Drake  - total words: {d_total}, unique words: {d_unique}, avg length: {d_avg_len:.2f}")
    print(f"Taylor - total words: {t_total}, unique words: {t_unique}, avg length: {t_avg_len:.2f}")

    # Step 5: Top words
    print_top_words(drake_freq, "Drake", 15)
    print_top_words(taylor_freq, "Taylor Swift", 15)

    # Step 6: ASCII bar charts
    ascii_bar_chart(drake_freq, "Drake", 15)
    ascii_bar_chart(taylor_freq, "Taylor Swift", 15)

    # Step 7: Cosine similarity
    sim = cosine_similarity(drake_freq, taylor_freq)
    print(f"\nCosine similarity between Drake and Taylor Swift Wikipedia pages: {sim:.4f}")


if __name__ == "__main__":
    main()
