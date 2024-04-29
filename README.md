# Home Work №8 - NoSQL

## Instructions

Part 1

1. Navigate to qutoes_scraper, activate environment and import necessary libraries from requirements.txt
2. Run crawling process "python main.py" and wait till script stops working.
3. Navigate to project folder (HW9PARSERS) and provide correct cridentials for MongoDB connection string in config.ini
4. You can remove data from the authors and quotes schema if needed by running clear_db.py script
5. Run load_json.py to populate data from json files (located in json directory)
6. run search.py to launch program to search by author or tag. Type 'exit' to exit the loop

## First part:

There is JSON file with authors and their attributes: date and location of birth, short biography description.
authors.json:

```json
[
  {
    "fullname": "Albert Einstein",
    "born_date": "March 14, 1879",
    "born_location": "in Ulm, Germany",
    "description": "In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University of Zurich by 1909. His 1905 paper explaining the photoelectric effect, the basis of electronics, earned him the Nobel Prize in 1921. His first paper on Special Relativity Theory, also published in 1905, changed the world. After the rise of the Nazi party, Einstein made Princeton his permanent home, becoming a U.S. citizen in 1940. Einstein, a pacifist during World War I, stayed a firm proponent of social justice and responsibility. He chaired the Emergency Committee of Atomic Scientists, which organized to alert the public to the dangers of atomic warfare.At a symposium, he advised: \"In their struggle for the ethical good, teachers of religion must have the stature to give up the doctrine of a personal God, that is, give up that source of fear and hope which in the past placed such vast power in the hands of priests. In their labors they will have to avail themselves of those forces which are capable of cultivating the Good, the True, and the Beautiful in humanity itself. This is, to be sure a more difficult but an incomparably more worthy task . . . \" (\"Science, Philosophy and Religion, A Symposium,\" published by the Conference on Science, Philosophy and Religion in their Relation to the Democratic Way of Life, Inc., New York, 1941). In a letter to philosopher Eric Gutkind, dated Jan. 3, 1954, Einstein stated: \"The word god is for me nothing more than the expression and product of human weaknesses, the Bible a collection of honorable, but still primitive legends which are nevertheless pretty childish. No interpretation no matter how subtle can (for me) change this,\" (The Guardian, \"Childish superstition: Einstein's letter makes view of religion relatively clear,\" by James Randerson, May 13, 2008). D. 1955.While best known for his mass–energy equivalence formula E = mc2 (which has been dubbed \"the world's most famous equation\"), he received the 1921 Nobel Prize in Physics \"for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect\". The latter was pivotal in establishing quantum theory.Einstein thought that Newtonion mechanics was no longer enough to reconcile the laws of classical mechanics with the laws of the electromagnetic field. This led to the development of his special theory of relativity. He realized, however, that the principle of relativity could also be extended to gravitational fields, and with his subsequent theory of gravitation in 1916, he published a paper on the general theory of relativity. He continued to deal with problems of statistical mechanics and quantum theory, which led to his explanations of particle theory and the motion of molecules. He also investigated the thermal properties of light which laid the foundation of the photon theory of light.He was visiting the United States when Adolf Hitler came to power in 1933 and did not go back to Germany. On the eve of World War II, he endorsed a letter to President Franklin D. Roosevelt alerting him to the potential development of \"extremely powerful bombs of a new type\" and recommending that the U.S. begin similar research. This eventually led to what would become the Manhattan Project. Einstein supported defending the Allied forces, but largely denounced the idea of using the newly discovered nuclear fission as a weapon. Later, with Bertrand Russell, Einstein signed the Russell–Einstein Manifesto, which highlighted the danger of nuclear weapons."
  },
  {
    "fullname": "Steve Martin",
    "born_date": "August 14, 1945",
    "born_location": "in Waco, Texas, The United States",
    "description": "Stephen Glenn \"Steve\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer. He was raised in Southern California in a Baptist family, where his early influences were working at Disneyland and Knott's Berry Farm and working magic and comedy acts at these and other smaller venues in the area. His ascent to fame picked up when he became a writer for the Smothers Brothers Comedy Hour, and later became a frequent guest on the Tonight Show.In the 1970s, Martin performed his offbeat, absurdist comedy routines before packed houses on national tours. In the 1980s, having branched away from stand-up comedy, he became a successful actor, playwright, and juggler, and eventually earned Emmy, Grammy, and American Comedy awards."
  }
]
```

and there's following JSON file with quotes of this authors.
quotes.json:

```json
[
  {
    "tags": ["change", "deep-thoughts", "thinking", "world"],
    "author": "Albert Einstein",
    "quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
  },
  {
    "tags": ["inspirational", "life", "live", "miracle", "miracles"],
    "author": "Albert Einstein",
    "quote": "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"
  },
  {
    "tags": ["adulthood", "success", "value"],
    "author": "Albert Einstein",
    "quote": "“Try not to become a man of success. Rather become a man of value.”"
  },
  {
    "tags": ["humor", "obvious", "simile"],
    "author": "Steve Martin",
    "quote": "“A day without sunshine is like, you know, night.”"
  }
]
```

## Previous Task description.

1. Create cloud DB [Atlas MongoDB](https://www.mongodb.com/atlas/database)
2. With the [ODM Mongoengine](https://docs.mongoengine.org/) create models to store data from these files in a collections of authors and quotes.
3. Field of author should be not be defined as a String but [Reference fields](https://docs.mongoengine.org/guide/defining-documents.html?highlight=ReferenceField#reference%20-fields), where ObjectID is saved from the collection authors.
4. Create scripts for loading json files to cloud database.
5. Implement script to search quotes by tag, by author name or set of tags. Script should be run in endless loop and with the help of 'input' operator should take commands in the following format "command: value".
   For example:

- name: Steve Martin - find and return list of all quotes of Stieve Martin.
- tag: life, live - find and return list of quotes where tags life or live are present (note: without whitespaces between tags)
- exit - end script execution;

1. Output of search results only in format utf-8;

HW9 task description:
Using Scrapy framework perform scrapping of the site http://quotes.toscrape.com. You need to get 2 files: quotes.json and authors.json.
The structure of the files should completely copy the structure of json files from the previous task.
Execute the scripts to load the data from the json files.
Previous HW should work properly with the new one.
