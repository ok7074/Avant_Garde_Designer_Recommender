import pandas as pd
import src.code_packages.config as cf
import src.code_packages.designer_dna as dd
import src.code_packages.preprocess as pp
import src.code_packages.recommender as rc
import src.code_packages.embeddings as emb
import src.api_integration as ai


class ServiceImpl:

    def __init__(self):
        self.designer_images = []
        self._item_emb = None

    def data_prep_and_embed(self):
        df = pd.read_csv("data/articles.csv")

        processed_df = pp.preprocess_articles(df)
        final_df = processed_df

        designer_df = dd.make_designer_df()


        prepped_corpora = rc.build_corpora(final_df, designer_df)


        df_embeddings = emb.encode_texts(
            prepped_corpora.items_text,
            model_name=cf.SETTINGS.model_name,
        )
        designer_embeddings = emb.encode_texts(
            prepped_corpora.designers_text,
            model_name=cf.SETTINGS.model_name,
        )


        df_with_designers = rc.attach_compatible_designers(
            final_df,
            df_embeddings,
            designer_embeddings,
            designer_df.index,
        )


        self._item_emb = df_embeddings

        return df_with_designers

    def generate_recommendation(self, query, df):

        user_recommendations_dict = rc.recommend_from_query(
            user_query=query,
            df_with_designers=df,
            item_emb=self._item_emb,
        )

        return user_recommendations_dict["designers"]

    def search_and_return_images(self, designer_names):

        results = {}

        for idx, designer in enumerate(designer_names[:2]):
            images = []

            response = ai.make_api_call(
                params={"q": designer, "page": 1}
            )

            if not response or "pins" not in response:

                results[designer] = images
                continue

            for pin in response["pins"]:
                if len(images) < 5:
                    images.append(pin["url"])
                else:
                    break

            
            results[designer] = images

        return results

    def designer_article_text(self, name):
        return dd.designer_dna[name]