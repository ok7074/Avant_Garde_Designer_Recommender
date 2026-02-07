
from Service.ServiceImpl import ServiceImpl

class ControllerImpl:

    def __init__(self):
        self.service = ServiceImpl()
        self.__preppedData = self.service.data_prep_and_embed()

    def make_recommendation(self, query):
        designer_names = self.service.generate_recommendation(
            query=query,
            df=self.__preppedData
        )
        return designer_names



