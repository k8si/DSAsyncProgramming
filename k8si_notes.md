* General: The writing could use another pass through. I made edits to the first half but the second half could use more work. There are a lot of places where you could simplify the writing by getting rid of extraneous adverbs and adjectives and switching from passive to active voice. For example, in the "Asynchronous Web-Scraping" section, you could simplify this sentence:
        "It is possible that some servers will take longer to process our requests than others"

    to:
        "Some servers may take longer to process requests than others"

    And in my opinion, you don't need this transition paragraph:

        "In this section we will also be introduced with another module supporting asynchronous programming options: `aiohttp` (which stands for Asynchronous I/O HTTP). This module provides high-level functionalities that streamline HTTP communication procedures, and it additionally works really well with the `asyncio` module to facilitate asynchronous programming."


* Prerequisites: I had trouble getting some of the code blocks to run in jupyter without a weird error message using Python 3.6. The quickest fix I found was downgrading to tornado==4.5.3. There's a ticket about this issue here: https://github.com/jupyter/notebook/issues/3397. Readers will also have to install aiohttp and aiofiles. I recommend just pointing the reader at the `requirements.txt` I added to the repo.

* Fibonacci example: "However, when analyzing the execution time obtained from the two versions of our Fibonacci-finding program, it was actually the sequential version that resulted in better speed. " -- This wasn't the case on my computer (sequential took 12.55 s, async took 12.31). Since the execution times are so close, it might depend on the environment. That's why I changed this part a bit.

* You might want to spend some time talking about the difference between concurrency vs. parallelism. You hint at this difference in the "CPU-Bound and Blocking Tasks" section but you could address it more directly.

* Is a task the same thing as a coroutine? Is there a formal definition of "task"?

* Unless you want to explain the difference between multithreading and multiprocessing, you should pick one of "multithreading" or "multiprocessing" (and quickly note somewhere that `concurrent.futures` supports both). It's cumbersome to read "multithreading/multiprocessing" and "threads/processes" in so many places.

* In the "Fetching a Website's HTML Code", the first code block will hang if you're running it behind a proxy (which will be the case for many readers who are at work).

* In the conclusion section, I suggest adding links to additional reading/resources like API docs and other blog posts about the subject.