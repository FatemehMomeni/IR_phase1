from .constructor import BSBIIndex

DATASET_PATH = 'D:/Mine/computerUI/terms/term8/information retrieval & web search/project/فاز اول و دوم/Dataset_IR'
OUTPUT_DIR = 'D:/Mine/computerUI/terms/term8/information retrieval & web search/project/phase1'


if __name__ == '__main__':
    BSBI_instance = BSBIIndex(data_dir=DATASET_PATH, output_dir=OUTPUT_DIR)
    query = input('search >>  ')
    result = BSBI_instance.retrieve(query)

