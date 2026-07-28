import traceback
import logging
import time


def log_exception(e: Exception, verbose: bool = False) -> None:
    """
    Logs the exception with a full traceback and a nicely formatted explanation.
    Args:
        e (Exception): The exception to log.
        verbose (bool): If True, logs the full traceback and explanation. If False, logs only the explanation.
    Returns:
        None
    """
    # Set up logging configuration
    logging.basicConfig(
        filename="traceback.txt",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    time_ = time.strftime("%Y-%m-%d %H:%M:%S")
    if verbose:

        # Log the exact local time of the exception (at {time of logging} an exception of type {type(e).__name__} occurred. Arguments:\n{e.args})
        logging.error(
            f"At {time_} an exception of type %s occurred. Arguments:\n%s",
            traceback.format_exc(),
            type(e).__name__,
            e.args,
        )

        # Log the full traceback
        logging.error("Traceback (most recent call last):\n%s", traceback.format_exc())

        # Write the explanation of the exception to the log file
        with open("traceback.txt", "a") as f:
            f.write(
                f"At {time_} an exception of type {type(e).__name__} occurred. Arguments:\n{e.args}\n"
            )
            f.write(f"Traceback (most recent call last):\n{traceback.format_exc()}\n")
            f.write("\n" + "-" * 25 + "\n")

        print("Exception logged to traceback.txt\n\n")

    else:
        # Log only the explanation
        logging.error(
            f"\nAt {time_} an exception of type %s occurred. Arguments:\n%s",
            type(e).__name__,
            e.args,
        )


# testing
if __name__ == "__main__":
    try:
        # Generate an exception for testing
        1 / 0
    except Exception as e:
        log_exception(e, verbose=True)
        log_exception(e, verbose=False)