def muzero(config: MuZeroConfig)
    storage = SharedStorage()
    replay_buffer = ReplayBuffer(config)
    
for _ in range(config.num_actors):
    launch_job(run_selfplay, config, storage, replay_buffer)

train_network(config, storage, replay_buffer)

return storage.latest_network()

