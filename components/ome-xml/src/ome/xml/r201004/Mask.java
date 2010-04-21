/*
 * ome.xml.r201004.Mask
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

public class Mask extends Shape
{
	// -- Instance variables --

	// Property
	private Double y;

	// Property
	private Double x;

	// Property which occurs more than once
	private List<String> binDataList = new ArrayList<String>();

	// -- Constructors --

	/** Default constructor. */
	public Mask()
	{
		super();
	}

	/** 
	 * Constructs Mask recursively from an XML DOM tree.
	 * @param element Root of the XML DOM tree to construct a model object
	 * graph from.
	 * @throws EnumerationException If there is an error instantiating an
	 * enumeration during model object creation.
	 */
	public Mask(Element element) throws EnumerationException
	{
		super(element);
		String tagName = element.getTagName();
		if (!"Mask".equals(tagName))
		{
			// TODO: Should be its own Exception
			throw new RuntimeException(String.format(
					"Expecting node name of Mask got %s",
					tagName));
		}
		if (element.hasAttribute("Y"))
		{
			// Attribute property Y
			setY(Double.valueOf(
					element.getAttribute("Y")));
		}
		if (element.hasAttribute("X"))
		{
			// Attribute property X
			setX(Double.valueOf(
					element.getAttribute("X")));
		}
		// Element property BinData which is not complex (has no
		// sub-elements) which occurs more than once
		NodeList BinData_nodeList = element.getElementsByTagName("BinData");
		for (int i = 0; i < BinData_nodeList.getLength(); i++)
		{
			addBinData(new String(
					BinData_nodeList.item(i).getTextContent()));
		}
	}

	// -- Mask API methods --

	// Property
	public Double getY()
	{
		return y;
	}

	public void setY(Double y)
	{
		this.y = y;
	}

	// Property
	public Double getX()
	{
		return x;
	}

	public void setX(Double x)
	{
		this.x = x;
	}

	// Property which occurs more than once
	public int sizeOfBinDataList()
	{
		return binDataList.size();
	}

	public List<String> copyBinDataList()
	{
		return new ArrayList<String>(binDataList);
	}

	public String getBinData(int index)
	{
		return binDataList.get(index);
	}

	public String setBinData(int index, String binData)
	{
		return binDataList.set(index, binData);
	}

	public void addBinData(String binData)
	{
		binDataList.add(binData);
	}

	public void removeBinData(String binData)
	{
		binDataList.remove(binData);
	}

	public Element asXMLElement(Document document)
	{
		return asXMLElement(document, null);
	}

	protected Element asXMLElement(Document document, Element Mask_element)
	{
		// Creating XML block for Mask
		if (Mask_element == null)
		{
			Mask_element = document.createElement("Mask");
		}
		Mask_element = super.asXMLElement(document, Mask_element);

		if (y != null)
		{
			// Attribute property Y
			Mask_element.setAttribute("Y", y.toString());
		}
		if (x != null)
		{
			// Attribute property X
			Mask_element.setAttribute("X", x.toString());
		}
		if (binDataList != null)
		{
			// Element property BinData which is not complex (has no
			// sub-elements) which occurs more than once
			for (String binDataList_value : binDataList)
			{
				Element binDataList_element = document.createElement("BinData");
				binDataList_element.setTextContent(binDataList_value);
				Mask_element.appendChild(binDataList_element);
			}
		}
		return Mask_element;
	}
}