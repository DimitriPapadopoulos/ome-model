/*
 * #%L
 * OME-XML Java library for working with OME-XML metadata structures.
 * %%
 * Copyright (C) 2006 - 2012 Open Microscopy Environment:
 *   - Massachusetts Institute of Technology
 *   - National Institutes of Health
 *   - University of Dundee
 *   - Board of Regents of the University of Wisconsin-Madison
 *   - Glencoe Software, Inc.
 * %%
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 * 
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 * 
 * The views and conclusions contained in the software and documentation are
 * those of the authors and should not be interpreted as representing official
 * policies, either expressed or implied, of any organization.
 * #L%
 */

/*-----------------------------------------------------------------------------
 *
 * THIS IS AUTOMATICALLY GENERATED CODE.  DO NOT MODIFY.
 * Created by melissa via xsd-fu on 2012-01-12 20:06:01-0500
 *
 *-----------------------------------------------------------------------------
 */

package ome.xml.model;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import ome.xml.model.enums.*;
import ome.xml.model.primitives.*;

public class Path extends Shape
{
	// Base:  -- Name: Path -- Type: Path -- javaBase: AbstractOMEModelObject -- javaType: Object

	// -- Constants --

	public static final String NAMESPACE = "http://www.openmicroscopy.org/Schemas/ROI/2011-06";

	/** Logger for this class. */
	private static final Logger LOGGER =
		LoggerFactory.getLogger(Path.class);

	// -- Instance variables --


	// Property
	private String definition;

	// -- Constructors --

	/** Default constructor. */
	public Path()
	{
		super();
	}

	/** 
	 * Constructs Path recursively from an XML DOM tree.
	 * @param element Root of the XML DOM tree to construct a model object
	 * graph from.
	 * @param model Handler for the OME model which keeps track of instances
	 * and references seen during object population.
	 * @throws EnumerationException If there is an error instantiating an
	 * enumeration during model object creation.
	 */
	public Path(Element element, OMEModel model)
	    throws EnumerationException
	{
		update(element, model);
	}

	// -- Custom content from Path specific template --


	// -- OMEModelObject API methods --

	/** 
	 * Updates Path recursively from an XML DOM tree. <b>NOTE:</b> No
	 * properties are removed, only added or updated.
	 * @param element Root of the XML DOM tree to construct a model object
	 * graph from.
	 * @param model Handler for the OME model which keeps track of instances
	 * and references seen during object population.
	 * @throws EnumerationException If there is an error instantiating an
	 * enumeration during model object creation.
	 */
	public void update(Element element, OMEModel model)
	    throws EnumerationException
	{
		super.update(element, model);
		String tagName = element.getTagName();
		if (!"Path".equals(tagName))
		{
			LOGGER.debug("Expecting node name of Path got {}", tagName);
		}
		if (element.hasAttribute("Definition"))
		{
			// Attribute property Definition
			setDefinition(String.valueOf(
					element.getAttribute("Definition")));
		}
	}

	// -- Path API methods --

	public boolean link(Reference reference, OMEModelObject o)
	{
		boolean wasHandledBySuperClass = super.link(reference, o);
		if (wasHandledBySuperClass)
		{
			return true;
		}
		LOGGER.debug("Unable to handle reference of type: {}", reference.getClass());
		return false;
	}


	// Property
	public String getDefinition()
	{
		return definition;
	}

	public void setDefinition(String definition)
	{
		this.definition = definition;
	}

	public Element asXMLElement(Document document)
	{
		return asXMLElement(document, null);
	}

	protected Element asXMLElement(Document document, Element Path_element)
	{
		// Creating XML block for Path

		if (Path_element == null)
		{
			Path_element =
					document.createElementNS(NAMESPACE, "Path");
		}

		if (definition != null)
		{
			// Attribute property Definition
			Path_element.setAttribute("Definition", definition.toString());
		}
		return super.asXMLElement(document, Path_element);
	}
}
