from flask import Flask, request, url_for, redirect, render_template
from collections import defaultdict

app = Flask(__name__, template_folder='templates')

@app.route("/", methods = ['POST', 'GET'])
def welcome():
    if request.method == 'POST':
      word = request.form['word']
      ret_val = is_pyramid(word)
      positive = '' if ret_val else ' not'
      result = 'String ' +  word + ' is' + positive + ' a pyramid word.'
      return render_template('goback.html', result = result)
    else:
      return render_template('pyramid.html')


def is_pyramid(word):
    #time complexity: O(n)
    if not word:
        # empty word
        return False
    word2counts = defaultdict(int)
    for char in word:
        word2counts[char] += 1
    countset = set(word2counts.values())
    if len(countset) != len(word2counts):
        # have duplicates
        return False
    if sum(countset) != len(countset) * (len(countset) + 1) // 2:
        # sum == n*(n+1)//2
        return False
    else:
        return True


if __name__ == "__main__":
    app.run()
