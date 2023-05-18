## Usage:

[Run or Google Codelab](https://colab.research.google.com/drive/1WPJyUBqYP-olKSwZxjbkJ0S-Nw_GMAzJ?usp=sharing)


OR
<br>

Run the program alone with random data or with optional arguments. Order of arguments does not matter.

```python
python paging.py
````

```python
python paging.py -OPTION <value> -OPTION <value> -OPTION <value> ...
````

### Specify number of pages.
This sets the size of the list of pages.

```python
python paging.py -np <int>
````

### Specify number of frames.
This sets the size of memory; the number of frames that pages can be swapped in/out of.

```python
python paging.py -nf <int>
````

### Specify number range of randomly generated pages.
Page numbers will range from min to max. *No negative numbers.

```python
python paging.py -pvr <int>
````

### Specify the pages.
Manually enter the pages to use with the alogorithms.

```python
python paging.py -p <int-1> <int-2> ... <int-k>
````

### Usage Examples:

```python
python paging.py
````

```python
python paging.py -p 5 5 5 1 5 6 3 2 8 7 -nf 4
````

```python
python paging.py -np 7 -nf 3
````

```python
python paging.py -np 7 -nf 3 -pvr 1 9
````

```python
python paging.py -nf 3 -p 1 1 1 2 5 6 3 7 8 9 9 5 4 2 1
````
