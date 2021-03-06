# โ๏ธ Inside Francis Bacon ๐ฅ



### ๐จ๏ธ... Seeing Through His Words

 โญ 2021.12  **OSS Term Project** by Hyebin Lee โญ

<br>

**<์ํ์๊ฐ>**

  **"์ธ์ด๋ ์ฌ๊ณ ์ ๊ฒฐ๊ณผ์ด๋ค"**, ๋๋ **"์ธ์ด๊ฐ ์ฌ๊ณ ๋ฅผ ์ง๋ฐฐํ๋ค"** ์ ๊ฐ์ ๋ง์ด ์์ต๋๋ค.  ์ค์ ๋ก ํ ์ฌ๋์ด ์ฌ์ฉํ๋ ๋จ์ด์ ์ธ์ด๋ ํด๋น ์ธ๋ฌผ์ด ์ด๋ค ๊ฐ์น๊ด๊ณผ ์ถ์ ์ถ๊ตฌํ๋ ์ง๋ฅผ ์ ์ ์๋ ์ ์ฉํ ํ๋จ ์งํ๊ฐ ๋๊ธฐ๋ ํฉ๋๋ค. 

  ์ด๋ฒ Term Project์์๋ ๋ณธ์ธ์ด ์ด๋ฒ ํ๊ธฐ ๊ต์  `๊ณผํ๊ธฐ์ ๊ณผ์ฌํ` ์์์์ ํนํ ์ธ์๊น๊ฒ ์ฝ์  `'์๋ก์ด ์ํ๋ํฐ์ค(The New Atlantis)'` ์ ์ ์์ด์ ์๊ตญ์ ์ฒ ํ์/๊ณผํ์์๋ **ํ๋์์ค ๋ฒ ์ด์ปจ (Francis Bacon, 1561~1626)** ์ ๊ธ์ ์ฌ์ฉ๋ ๋จ์ด๋ค์ ์ข๋ฅ์ ๋น๋์๋ฅผ _Python_ ๊ณผ ์ด์ ๋ค์ํ ํดํท์ ํตํด ์ ๋์ ์ผ๋ก ๋ถ์ํ๊ณ  ์ด๋ฅผ ์๊ฐํํ์ฌ ๊ทธ๊ฐ ์ถ๊ตฌํ๋ ์ฌ์๊ณผ ์ถ์ ๋ฐฉํฅ์ ์์๋ณด๊ณ ์ ํฉ๋๋ค.

<img title="" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Somer_Francis_Bacon.jpg/375px-Somer_Francis_Bacon.jpg" alt="" data-align="center">

<p>Francis Bacon, image from wikipedia</p>

## **Set Up & Prerequisites**

have used: 

* [Anaconda]([Anaconda | The World's Most Popular Data Science Platform](https://www.anaconda.com/))

* [NLTK (Natural Language Toolkit)]([NLTK :: Natural Language Toolkit](https://www.nltk.org/)) For extracting words and its frequency

* [Matplotlib]([Matplotlib โ Visualization with Python](https://matplotlib.org/)) For Visualization

* Bacon's Books (From [Project Gutenberg]([Free eBooks | Project Gutenberg](https://www.gutenberg.org/)))
  
  * The New Atlantis
  
  * The Advancement of Learning
  
  * Bacon's Essays, and Wisdom of the Ancients

#### Installing NLTK through Anaconda

ย ย ย ย ย ย ย ย Enter the following command in Anaconda prompt:

ย   ย ย ย ย `conda install -c anaconda nltk`

## Going Through the Words

I have attained three .txt files of Bacon's books through [Project Gutenberg]([Free eBooks | Project Gutenberg](https://www.gutenberg.org/)), so all the Copyright Rules are due to its terms of use.

* Tokenizing words with NLTK
  
  I got many help from [This](https://vitalflux.com/nltk-how-read-process-text-file/) website for reading text files and processing them with NLTK. But I have added my own additional conditions to produce more refined results.

* The code consists of :
  
  (It is also explained in the comment section in the code)
  
  * Reading the file (Tokenizing)
  
  * Calculating the Frequency Distribution
  
  * Plotting the words with their Frequency (Total)
  
  * Adding word length and frequency value conditions for analyzation
  
  * Eliminating useless words
  
  * Plotting the 'real' frequent words
  
  And this is about it!

* More explanation about word extract conditions and eliminating :
  
  I have set the word length conditions to having 7 or more characters since words less than 6 characters tend to have less sophisticated and less significant meanings for getting useful information about the text.
  
  For words that have no meaning but consists of 7 or more words, I have eliminated by adding `!=` conditions. It was all done by manually.
  
  | before                  | after                |
  |:-----------------------:|:--------------------:|
  | ![](./image/before.png) | ![](image/after.png) |
  
  Also I have decided the `fdist[word] >= (value)` 's  `(value)` considering the length of the book; so at each cases, the value is different.

## Results and Analyzation

* #### **Total Word Frequency**

| ![](./image/1-1.png) | ![](image/2-1.png)   |
| -------------------- | -------------------- |
| ![](./image/3-1.png) | ![](./image/4-1.png) |

In the Total Word Frequency graph, all four results consisted pretty much of same words due to grammatical reasons. Most of them were less than 4 words.

* #### **The Real Frequent Words**
  
  | The New Atlantis     | The Advancement of Learning |
  | -------------------- | --------------------------- |
  | ![](./image/1-2.png) | ![](./image/2-2.png)        |
  | **Bacon's Essays**   | **All Together**            |
  | ![](./image/3-2.png) | ![](./image/4-2.png)        |

## Conclusion

<img src="./image/4-2.png" title="" alt="" data-align="center">

The Frequent Words in each book were respectively:



**The New Atlantis**

[natural, inventor, marriage, knowledge, Bensalem, motions, kingdom, Salomon, experiments, humanity, country, creatures, chariot, chambers, instruments, imitate, artificial, voyages, victuals, servant, question, principal, offered, mixtures, governor, ancient, Strangers, Spanish, Saviour]



**The Advancement of Learning**
[learning, philosphy, natural, history, sciences, fortune, judgement, opinion, ancient, Aristotle, towards, government, invention, pleasure, further, subject, religion, purpose, nothing, whether, science, matters, imagination, divinity, greater, argument, princes, knowledges, Majesty, natures, doctrine, Scriptures]



**Bacon's Essays**

[buisness, counsel, natural, ancient, jupiter, philosophy, religion, England, judgement, fortune, country, present, children, justice, principal, authority, ancients, servants]



**All Together**, they were

[learning, natural, philosophy, buisness, fortune, ancient, judgement, history, religion, sciences, counsel, government, learned, Jupiter, invention, purpose, natures, Aristotle]



Through the output of words, we can **conclude** that Bacon was a true *seeker* for knowledge; (FYI: '์๋ ๊ฒ์ด ํ์ด๋ค'์ ์ฃผ์ธ์ด ๋ฐ๋ก ํ๋์์ค ๋ฒ ์ด์ปจ) 

And from the graph right above(Frequent Words - All Together), we can see that 'Aristotle' is in the list as well. 

As well known, Bacon denied the traditional Aristole's deductive theory ([์ฐธ๊ณ ](https://namu.wiki/w/%ED%94%84%EB%9E%9C%EC%8B%9C%EC%8A%A4%20%EB%B2%A0%EC%9D%B4%EC%BB%A8)) and stated that we can only believe facts that are proven through real observation and experiments. We can see the related set of words from the extracted words.

He was also interested in political philosohpy and ancient myths, and this also we can find in the wordlists. 

For more information about Francis Bacon you may read: [ํ๋์์ค ๋ฒ ์ด์ปจ : ๋ค์ด๋ฒ ํฌ์คํธ (naver.com)](https://post.naver.com/viewer/postView.naver?volumeNo=27958387&memberNo=9935567)







## ์ฐธ๊ณ ์๋ฃ/References

* [NLTK - How to Read & Process Text File - Data Analytics (vitalflux.com)](https://vitalflux.com/nltk-how-read-process-text-file/)

* [Free eBooks | Project Gutenberg](https://www.gutenberg.org/)

* [ํ๋ก์ ํธ ๊ตฌํ๋ฒ ๋ฅดํฌ - ์ํค๋ฐฑ๊ณผ, ์ฐ๋ฆฌ ๋ชจ๋์ ๋ฐฑ๊ณผ์ฌ์  (wikipedia.org)](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B5%AC%ED%85%90%EB%B2%A0%EB%A5%B4%ED%81%AC)

* [ํ๋์์ค ๋ฒ ์ด์ปจ - ์ํค๋ฐฑ๊ณผ, ์ฐ๋ฆฌ ๋ชจ๋์ ๋ฐฑ๊ณผ์ฌ์  (wikipedia.org)](https://ko.wikipedia.org/wiki/%ED%94%84%EB%9E%9C%EC%8B%9C%EC%8A%A4_%EB%B2%A0%EC%9D%B4%EC%BB%A8)
