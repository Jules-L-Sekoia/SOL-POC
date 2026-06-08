from sekoia_automation.module import Module

from SOL.create_dataset import CreateDataset
from SOL.delete_dataset import DeleteDataset
from SOL.execute_a_query import ExecuteAQuery
from SOL.list_queries import ListQueries
from SOL.models import SolModuleConfiguration


class SolModule(Module):
    configuration: SolModuleConfiguration


__all__ = [
    "SolModule",
    "SolModuleConfiguration",
    "CreateDataset",
    "DeleteDataset",
    "ExecuteAQuery",
    "ListQueries",
]
