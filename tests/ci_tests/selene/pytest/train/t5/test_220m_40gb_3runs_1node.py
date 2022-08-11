import os


BASE_RESULTS_DIR = os.environ.get("BASE_RESULTS_DIR")

class TestCIT5220m:

    def test_ci_train_t5_220m_80gb_3runs(self):
        base_cfg = os.path.join(BASE_RESULTS_DIR, "t5/0.22b_40gb/base_cfg_0.22b.yaml")
        candidate_configs_dir = os.path.join(BASE_RESULTS_DIR, "t5/0.22b_40gb/candidate_configs")
        training_logs_dir = os.path.join(BASE_RESULTS_DIR, "t5/0.22b_40gb/training_logs")
        final_result_dir = os.path.join(BASE_RESULTS_DIR, "t5/0.22b_40gb/final_result")
        final_summary_csv = os.path.join(BASE_RESULTS_DIR, "t5/0.22b_40gb/final_result/final_summary_1nodes.csv")
        optimal_cfg = os.path.join(BASE_RESULTS_DIR, "t5/0.22b_40gb/final_result/optimal_config_0.22b_1nodes.yaml")

        assert os.path.exists(base_cfg), f"File not found: {base_cfg}"
        assert os.path.exists(candidate_configs_dir), f"Dir not found: {candidate_configs_dir}"
        assert os.path.exists(training_logs_dir), f"Dir not found: {training_logs_dir}"
        assert os.path.exists(final_result_dir), f"Dir not found: {final_result_dir}"
        assert os.path.exists(final_summary_csv), f"File not found: {final_summary_csv}"
        assert os.path.exists(optimal_cfg), f"File not found: {optimal_cfg}"