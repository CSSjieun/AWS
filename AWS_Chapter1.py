import awswrangler as wr
import numpy as np
import pandas as pd

# df = wr.s3.read_parquet("s3://<BUCKET>/<DATASET>/")

# Amazon Personalize
# 수백만 개의 영화 평점이 담긴 인기 있는 훈련 데이터셋인 무비렌즈 MovieLens를 이용해 훈련된 아마존 퍼스널라이즈는 다음과 같은 추천 영화 결괏값을 생성한다.
get_recommendations_reponse = personalize_runtime.get_recommendations(
    campaignArn = "campaign_arn" #string
    userId = "user_id" #string
    
)

item_list = get_recommendations_response['itemList']
recommendation_list = []
for item in item_list:
    item_id = get_movie_by_id(item['itemList'])
recommendation_list.append(item_id)

# 다음 텐서플로우 추천기 라이브러리 사용 예제는 추천기로 평점을 예측(다음코드 예제의 rating_task 객체)하고 조회수를 예측(다음 코드 예제의 retrieve_task 객체)하도록 훈련시키는 방법을 보여준다.
user_model = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.StringLookup(
        vocabulary=unique_user_ids),
    #알 수 없는 토큰과 마스크 토큰을 처리하기 위해
    # unique_user_ids 리스트 사이즈에 2를 더한다.
    tf.keras.layers.Embedding(len(unique_user_ids) + 2, embedding_dimension)
])

movie_model = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.StringLookUp(
        vocabulary=unique_movie_titles),
    tf.keras.layers.Embedding(len(unique_movie_titles) + 2, embedding_dimension)
    
])

rating_task = tfrs.tasks.Ranking(
    loss=tf.keras.losses.MeanSquaredError(),
    metrics=[tf.keras.metrics.RootMeanSquaredError()],
)

retrieval_task = tfrs.tasks.Retrieval(
    metrics=tfrs.metrics.FacorizeTopK(
        candidates=movies.batch(128).map(self.movie_model)
    )
)


