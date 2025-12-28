import flwr as fl

class LoggingStrategy(fl.server.strategy.FedAvg):
    def aggregate_fit(self, server_round, results, failures):
        print(f"\n--- Server aggregating round {server_round} ---")
        return super().aggregate_fit(server_round, results, failures)

strategy = LoggingStrategy(
    fraction_fit=1.0,
    min_fit_clients=2,
    min_available_clients=2,
)

fl.server.start_server(
    server_address="127.0.0.1:8080",
    config=fl.server.ServerConfig(num_rounds=3),
    strategy=strategy,
)
