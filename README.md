# OME Data Model

[![Build Status](https://github.com/ome/ome-model/workflows/Maven/badge.svg)](https://github.com/ome/ome-model/actions)
[![Maven Central](https://img.shields.io/maven-central/v/org.openmicroscopy/ome-xml.svg)](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22org.openmicroscopy%22%20AND%20a%3A%22ome-xml%22)
[![Javadocs](http://javadoc.io/badge/org.openmicroscopy/ome-xml.svg)](http://javadoc.io/doc/org.openmicroscopy/ome-xml) 

OME data model specification, code generator and implementation.

Links
-----

- [Documentation](https://ome-model.readthedocs.io/en/stable/)
- [Java API reference](http://javadoc.io/doc/org.openmicroscopy/ome-xml/)
- [OME-TIFF sample images](https://downloads.openmicroscopy.org/images/OME-TIFF/)
- [OME-XML sample images](https://downloads.openmicroscopy.org/images/OME-XML/)

Contribute
----------

To contribute to the OME Model documentation, go to the [documentation repository](https://github.com/ome/ome-model-documentation).

Pull request testing
--------------------

We welcome pull requests from anyone, but ask that you please verify the
following before submitting a pull request:

 * verify that the branch merges cleanly into ```master```
 * verify that the branch compiles using Maven
 * verify that the branch does not use syntax or API specific to Java 1.8+
 * internal developers only: [run the data
   tests](https://bio-formats.readthedocs.io/en/stable/developers/commit-testing.html)
   against directories corresponding to the affected format(s)
 * make sure that your commits contain the correct authorship information and,
   if necessary, a signed-off-by line
 * make sure that the commit messages or pull request comment contains
   sufficient information for the reviewer(s) to understand what problem was
   fixed and how to test it
