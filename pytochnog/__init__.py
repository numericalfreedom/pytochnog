from pytochnog import *

""" @mainpage Interactive manual

 - @ref PAG_Basic_information
 - @ref SCT_How_to_get_started
 - @ref SCT_Pre_and_postprocessing

This is an interactive documentation for the Tochnog Professional finite element program.


@page PAG_Basic_information  Basic information
@tableofcontents

@section SCT_How_to_get_started  How to perform a calculation and how to get started

Create an input file, e.g. problem.dat. The default input file is tochnog.dat, which will be used
if no other input file is specified. Thus the command tochnog tochnog.dat yields output on the
screen while tochnog tochnog.dat > tochnog.out redirects the output to a file.
So to get started do, for example, the following:

 - cd test/other
 - tochnog condif1.dat

Use the condif1.dat test to get started.

 - Copy condif1.dat to tochnog.dat.
 - Use your favorite editor to open the file tochnog.dat and study it.
 - Change echo to -yes.
 - Remove the parentheses (...) surrounding the control_print statement and save the file.
 - Run by typing tochnog or tochnog tochnog or tochnog tochnog.dat.
 - Study the output on the screen.
 - Study the tochnog.log file.
 - Study the tochnog.dbs file. It contains the database after the calculation, and is an input
file itself!

Read at least once the start of the data part introduction section.


@section SCT_Pre_and_postprocessing  Pre- and postprocessing

You can use GID both for preprocessing (mesh generation) and post processing (plotting). GID
is commercially available at the www.gidhome.com Internet page. A free demo version of is
available for download.

Alternatively to GID you can use Mecway for preprocessing input_abaqus and post processing
control_print_gmsh. Mecway is commercially available at the mecway.com Internet page.
It is very affordable, and also has build in FE calculations (mostly for mechanical engineering). A
free demo version of Mecway is available for download.

You can also use GMSH both for preprocessing and post processing. GMSH is freely available
at www.geuz.org/gmsh.

Postprocessing files are written for the visualization program PARAVIEW. The PARAVIEW
program is freely available at www.paraview.org.

Furthermore. postprocessing files are written for the visualization program TECPLOT. These
TECPLOT are less well maintained then the files for other postprocessing programs.

With GNUPLOT you can plot files resulting from control_print_history and control_print_data_vers
Also any other x-y plotting program can be used for such files.

"""
