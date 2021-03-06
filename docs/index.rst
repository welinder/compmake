.. raw:: html
   :file: fork.html

.. container:: twitterbadge

   **Latest news**

   .. raw:: html
      :file: twitter_badge.html

.. include:: definitions.txt

Compmake
=========

|compmake| is a non-obtrusive module that provides:

* ``make``--like facilities to your Python computations (``make``, ``clean``, etc.),
  including caching of temporary results (that is, you can interrupt your program, and restart it without losing  (much) data.)
* A console for inspecting failures and partial completion.
* Single-host (using the ``multiprocessing`` module) and multiple-host parallelization (using ssh-spawned slaves).
* Peace of mind!

To use |compmake|, you have to minimally modify your Python program,
such that it can understand the processing layout and
the opportunities for parallelization.

.. image:: initial.png 
   :class: bigpicture

You would run the modified program using::

    $ compmake example make       # runs locally
    $ compmake example parmake    # runs locally in parallel
    $ compmake example clustmake  # runs on a cluster

You can selectively remake part of the computations. For example,
suppose that you modify the ``draw()`` function, and you want to
rerun only the last step. You can achieve that by::

    $ compmake example remake "draw*"

|compmake| will reuse part of the computations (``func1`` and ``func2``)
but it will redo the last step.

Moreover, by running ``compmake example`` only, you have access to a
console that allows you to inspect the status of the computations,
cleaning/remaking jobs, etc.

|compmake| has been designed primarily for handling long computational-intensive
batch processes. It assumes that the computational layout is fixed and that 
all intermediate results can be cached to disk. If these two conditions are met,
you can use |compmake| to gain considerable peace of mind.

Still not convinced? Read :ref:`why`.

Still interested? Read along. Start with the tutorial :ref:`tutorial_basic`.
And check out :ref:`limitations` to see if ``compmake`` can help you.



**Note**: |compmake| is currently an **alpha release**:
while most of the functionality is there,
the documentation is not complete,
it is a bit rough around the edges,
and some minor aspects of the API could change in the future.
If you feel adventorous, this is a perfect time to
get support and influence |compmake|'s evolution!


.. container:: col1

	**Getting started**

	* :ref:`install`
	* :ref:`why`
	* :ref:`limitations`

	**Tutorial**
	
	* :ref:`tutorial_basic`
	* :ref:`tutorial_console`
	* :ref:`tutorial_parmake`
	* :ref:`tutorial_embedding`

.. container:: col2

	**Advanced usage**

	* :ref:`tutorial_cluster`
	* :ref:`tutorial_suspend`
	* :ref:`tutorial_more`

	**Reference**

	* :ref:`commands`
	* :ref:`config`

	**Developer**

	* :ref:`developer`
	* :ref:`extending`
	* :ref:`building_docs`

.. raw:: html

   <div style="clear:left"/>

Quick installation
------------------

The quick install is::

$ easy_install compmake

This will allow you to run |compmake| on a single host.
However, there are also separate dependencies to install for some
advanced features such as multiprocessing. See :ref:`install` for more information.


Source download
+++++++++++++++

Development happens on github: http://github.com/AndreaCensi/compmake

.. raw:: html
   :file: download.html


Feedback
---------

Compmake is currently developed by `Andrea Censi`_. Contributors are most welcome.

Please use the `issue tracker on github`_ for bugs and requested features.

.. _`issue tracker on github`: http://github.com/AndreaCensi/compmake/issues

.. _`Andrea Censi`: http://www.cds.caltech.edu/~andrea/
 
.. toctree::
   :hidden:
   :glob:

   install*
   features*
   tutorial*
   config*
   commands*
   *



* :ref:`search`

