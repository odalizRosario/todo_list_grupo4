from src.todo_list.methods import file_functions

import pandas as pd
import pytest
import shutil


@pytest.fixture(scope="function")
def mk_tmp_dir(tmpdir_factory):
    """

    Parameters
    ----------
    tmpdir_factory :
        

    Returns
    -------

    """
    my_tmpdir = tmpdir_factory.mktemp("pytestdata")
    file_functions.PATH_TO_DATA = str(my_tmpdir)
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))


@pytest.fixture(scope="session")
def df_empty():
    """

    Parameters
    ----------
    tmp_dir :
        
    df_empty :
        

    Returns
    -------

    """
    
        
    return pd.DataFrame(
        columns=["created", "task", "summary", "status", "owner"])


@pytest.fixture(scope="function")
def df_empty_stored(tmp_dir, df_empty):
    """

    Parameters
    ----------
    tmp_dir :
        
    df_empty :
        

    Returns
    -------

    """
    df_empty.to_csv(f"{tmp_dir}/todos.csv", index=False)
    return df_empty


def check_list_exists(df_empty_stored):
    """

    Parameters
    ----------
    df_empty_stored :
        

    Returns
    -------

    """
    assert file_functions.check_list_exists("todos") == True


def get_list_path():
    """ """
    assert file_functions.get_list_path("todos") == \
        file_functions.PATH_TO_DATA + "/" + "todos.csv"


def get_filename():
    """

    Parameters
    ----------
    tmp_dir :
        
    df_empty :
        

    Returns
    -------

    """
    assert file_functions.get_list_filename("data") == "data.csv"

    return pd.DataFrame(
        columns=["created", "task", "summary", "status", "owner"])



def load_list(df_empty_stored, tmp_dir):
    """

    Parameters
    ----------
    tmp_dir :
        

    Returns
    -------

    """
    df = file_functions.load_list("todos")
    pd.testing.assert_frame_equal(df_empty_stored, df)


def check_number_of_files(df_empty_stored):
    """

    Parameters
    ----------
    df_empty_stored :
        

    Returns
    -------

    """
    assert len(file_functions.get_existing_lists()) == 1
