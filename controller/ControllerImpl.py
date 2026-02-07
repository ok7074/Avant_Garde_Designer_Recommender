import requests
from Service.ServiceImpl import ServiceImpl
import os
from dotenv import load_dotenv


@dataclass
class ControllerImpl():
    service : ServiceImpl()
    designerNames: list[str]

    def __init__(self, prepped_data):
        self.__preppedData=service.data_prep_and_embed()


    def make_recommendation(self, query, df):
        self.designerNames=service.generate_recommendation(query,df)
        return self.designerNames







