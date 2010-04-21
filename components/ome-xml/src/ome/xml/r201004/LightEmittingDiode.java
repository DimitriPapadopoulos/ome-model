/*
 * ome.xml.r201004.LightEmittingDiode
 *
 *-----------------------------------------------------------------------------
 *
 *  Copyright (C) @year@ Open Microscopy Environment
 *      Massachusetts Institute of Technology,
 *      National Institutes of Health,
 *      University of Dundee,
 *      University of Wisconsin-Madison
 *
 *
 *
 *    This library is free software; you can redistribute it and/or
 *    modify it under the terms of the GNU Lesser General Public
 *    License as published by the Free Software Foundation; either
 *    version 2.1 of the License, or (at your option) any later version.
 *
 *    This library is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *    Lesser General Public License for more details.
 *
 *    You should have received a copy of the GNU Lesser General Public
 *    License along with this library; if not, write to the Free Software
 *    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 *-----------------------------------------------------------------------------
 */

/*-----------------------------------------------------------------------------
 *
 * THIS IS AUTOMATICALLY GENERATED CODE.  DO NOT MODIFY.
 * Created by callan via xsd-fu on 2010-04-21 11:45:19+0100
 *
 *-----------------------------------------------------------------------------
 */

package ome.xml.r201004;

import java.util.ArrayList;
import java.util.List;


import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import ome.xml.r201004.enums.*;

public class LightEmittingDiode extends LightSource
{
	// -- Instance variables --

	// -- Constructors --

	/** Default constructor. */
	public LightEmittingDiode()
	{
		super();
	}

	/** 
	 * Constructs LightEmittingDiode recursively from an XML DOM tree.
	 * @param element Root of the XML DOM tree to construct a model object
	 * graph from.
	 * @throws EnumerationException If there is an error instantiating an
	 * enumeration during model object creation.
	 */
	public LightEmittingDiode(Element element) throws EnumerationException
	{
		super(element);
		String tagName = element.getTagName();
		if (!"LightEmittingDiode".equals(tagName))
		{
			// TODO: Should be its own Exception
			throw new RuntimeException(String.format(
					"Expecting node name of LightEmittingDiode got %s",
					tagName));
		}
	}

	// -- LightEmittingDiode API methods --

	public Element asXMLElement(Document document)
	{
		return asXMLElement(document, null);
	}

	protected Element asXMLElement(Document document, Element LightEmittingDiode_element)
	{
		// Creating XML block for LightEmittingDiode
		if (LightEmittingDiode_element == null)
		{
			LightEmittingDiode_element = document.createElement("LightEmittingDiode");
		}
		LightEmittingDiode_element = super.asXMLElement(document, LightEmittingDiode_element);

		return LightEmittingDiode_element;
	}
}