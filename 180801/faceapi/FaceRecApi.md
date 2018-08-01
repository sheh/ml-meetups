[**Cognitive Services Microsoft**](https://azure.microsoft.com/ru-ru/pricing/details/cognitive-services/face-api/)

*Функции:*

- Face verification
- Face detection (landmarks)
- Emotion recognition
- Face identification (Face API enables you to search, identify and match faces in your private repository of up to 1 million people.)
- Similar face search (Easily find similar-looking faces. Given a collection of faces and a new face as a query, this API will return a collection of similar faces. )
- Face grouping (Organise many unidentified faces together into groups, based on their visual similarity.)



*Стоимость*
* Бесплатно: до 20 транзакций в минуту.	**Бесплатных транзакций в месяц: 30 000**
* Платно: до 10 транзакций в секунду и до **62,50 за 1000 транзакций**, если транзакций меньше 1М, дальше дешевле


*SDKs:*

- CSharp
- Java для Android
- Python



[**Google Cloud Vision API**](https://cloud.google.com/vision/)

*Функции:*

- Face detection
- Facial Recognition **is NOT supported**
- Emotion likeloods (joyLikelihood, sorrowLikelihood, ...)

*Стоимость (Facial Detection)*
- Free: 1 - 1,000 UNITS/MONTH 
- Paid: 1001 - 5 MILLION UNITS/MONTH - **1.5$ per 1,000**, 5+ MILLION UNITS/MONTH - **0.6$ per 1,000**


*SDKs:*

- C#
- GO
- Java
- Node.js
- PHP
- Python
- Ruby



[**Amazon Rekognition**](https://aws.amazon.com/rekognition/?nc1=h_ls)

*Функции:*

- Detect emotions 
- Face-based user verification
- Search image library
- Pathing on video

*Стоимость*
* First 1 million images processed* per month - **$1 per 1,000 images**

*SDKs:*

- C#
- GO
- Java
- Node.js
- PHP
- Python
- Ruby
- CLI


[**Face classification** (open source MIT)](https://github.com/oarriaga/face_classification)

*Функции:*

- Face detection
- Detect emotions

*SDKs:*
- hdf5 files


**Sunny day test set, positive/negative emotion classes**

microsoft

positive: 100.0%
negative: 61.7%

positive + negative: 77.9%


face_classification (opensource + face detection tuning)

positive: 88.6%
negative: 60.0%
positive + negative: 72.1%


aws

positive: 95.5%
negative: 48.3%
positive + negative: 68.3%


Выводы:

- провайдеры api довольно дороги, аналитика по 8 часам записи с камеры с fps 2-3 будет стоить порядка 80-90$
- заметно лучше определяются положительные эмоции
- точночть определения пола довольно высокая
- точность определения возроста низкая


Ссылки:

- [fer2013](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)
- [Microsoft FERPlus](https://github.com/Microsoft/FERPlus)
- [Amazon’s facial recognition matched 28 members of Congress to criminal mugshots](https://www.theverge.com/2018/7/26/17615634/amazon-rekognition-aclu-mug-shot-congress-facial-recognition)
