import click
from SGD dataset.train.create_data import NLU_Createdata

@click.group()
def cli1():
    pass

@cli1.command()

#In default 'Relative Path' of the Testsuit and Testcase has provided(from os module '../' represents one level up to the current Working directory)
@click.option('--infile', default = 'SGD dataset/train/train_1_01.json', help = 'Loading JSON file in the specified path')
@click.option('--outnlu', default = 'NLU_traindata.json', help = 'output customized JSON file in the specified path')
@click.option('--outdm', default = 'DM_stories.md', help = 'output customized conversation as md file in the specified path')
@click.option('--outnlg', default = 'NLG_traindata.json', help = 'output customized NLG as JSON file in the specified path')


def format(infile, outnlu, outdm, outnlg):
    print("The annotated data for training will be loaded from: ", infile)
    NLU_Createdata.custom_sgd(infile,outnlu)
    #dm_storycreator.DM_Createstory.story_create(infile,outdm)
    #nlg_datacreator.NLG_Createdata.nlg_createdata(infile,outnlg)  
    
if __name__ == '__main__':
     cli1()