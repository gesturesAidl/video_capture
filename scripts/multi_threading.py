import threading

class VideoProcessor:

    def process(self):
        try:
            threads = []
            feature_extraction = threading.Thread(target=extract_features(), args=[input_data_features])
            threads.append(feature_extraction)
            feature_extraction.start()

            optical_flow_calc = threading.Thread(target=extract_optical_flow(), args=[input_data_optical_flow])
            threads.append(optical_flow_calc)
            optical_flow_calc.start()

        except Exception as e:
            print(str(e))

        # Blocking main thread until all processes in threads[] have been performed.
        for thread in threads:
            thread.join()
