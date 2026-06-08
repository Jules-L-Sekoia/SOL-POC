from sekoia_automation.module import Module

from SOL import (
    ListQueries,
    ExecuteAQuery,
    DeleteDataset,
    CreateDataset,
    SolModule,
)


if __name__ == "__main__":
    module = SolModule()
    module.register(CreateDataset, "create-dataset")
    module.register(ListQueries, "list-queries")
    module.register(ExecuteAQuery, "execute-a-query")
    module.register(DeleteDataset, "delete-dataset")
    module.run()
