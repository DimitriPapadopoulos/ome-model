/*
 * ome.xml.r201004.Plane
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
 * Created by callan via xsd-fu on 2010-04-23 17:06:57+0100
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

public class Plane extends AbstractOMEModelObject
{
	// -- Constants --

	public static final String NAMESPACE = "http://www.openmicroscopy.org/Schemas/OME/2010-04";

	// -- Instance variables --

	// Property
	private Double exposureTime;

	// Property
	private Double positionZ;

	// Property
	private Double positionX;

	// Property
	private Double positionY;

	// Property
	private Double deltaT;

	// Property
	private Integer theC;

	// Property
	private Integer theZ;

	// Property
	private Integer theT;

	// Property
	private String hashSHA1;

	// Reference AnnotationRef
	private List<Annotation> annotationList = new ArrayList<Annotation>();

	// -- Constructors --

	/** Default constructor. */
	public Plane()
	{
		super();
	}

	/** 
	 * Constructs Plane recursively from an XML DOM tree.
	 * @param element Root of the XML DOM tree to construct a model object
	 * graph from.
	 * @param model Handler for the OME model which keeps track of instances
	 * and references seen during object population.
	 * @throws EnumerationException If there is an error instantiating an
	 * enumeration during model object creation.
	 */
	public Plane(Element element, OMEModel model)
	    throws EnumerationException
	{
		update(element, model);
	}
	
	// -- Custom content from Plane specific template --


	// -- OMEModelObject API methods --

	/** 
	 * Updates Plane recursively from an XML DOM tree. <b>NOTE:</b> No
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
		super.update(element);
		String tagName = element.getTagName();
		if (!"Plane".equals(tagName))
		{
			System.err.println(String.format(
					"WARNING: Expecting node name of Plane got %s",
					tagName));
			// TODO: Should be its own Exception
			//throw new RuntimeException(String.format(
			//		"Expecting node name of Plane got %s",
			//		tagName));
		}
		if (element.hasAttribute("ExposureTime"))
		{
			// Attribute property ExposureTime
			setExposureTime(Double.valueOf(
					element.getAttribute("ExposureTime")));
		}
		if (element.hasAttribute("PositionZ"))
		{
			// Attribute property PositionZ
			setPositionZ(Double.valueOf(
					element.getAttribute("PositionZ")));
		}
		if (element.hasAttribute("PositionX"))
		{
			// Attribute property PositionX
			setPositionX(Double.valueOf(
					element.getAttribute("PositionX")));
		}
		if (element.hasAttribute("PositionY"))
		{
			// Attribute property PositionY
			setPositionY(Double.valueOf(
					element.getAttribute("PositionY")));
		}
		if (element.hasAttribute("DeltaT"))
		{
			// Attribute property DeltaT
			setDeltaT(Double.valueOf(
					element.getAttribute("DeltaT")));
		}
		if (element.hasAttribute("TheC"))
		{
			// Attribute property TheC
			setTheC(Integer.valueOf(
					element.getAttribute("TheC")));
		}
		if (element.hasAttribute("TheZ"))
		{
			// Attribute property TheZ
			setTheZ(Integer.valueOf(
					element.getAttribute("TheZ")));
		}
		if (element.hasAttribute("TheT"))
		{
			// Attribute property TheT
			setTheT(Integer.valueOf(
					element.getAttribute("TheT")));
		}
		NodeList HashSHA1_nodeList = element.getElementsByTagName("HashSHA1");
		if (HashSHA1_nodeList.getLength() > 1)
		{
			// TODO: Should be its own Exception
			throw new RuntimeException(String.format(
					"HashSHA1 node list size %d != 1",
					HashSHA1_nodeList.getLength()));
		}
		else if (HashSHA1_nodeList.getLength() != 0)
		{
			// Element property HashSHA1 which is not complex (has no
			// sub-elements)
			setHashSHA1(HashSHA1_nodeList.item(0).getTextContent());
		}
		// Element reference AnnotationRef
		NodeList AnnotationRef_nodeList = element.getElementsByTagName("AnnotationRef");
		for (int i = 0; i < AnnotationRef_nodeList.getLength(); i++)
		{
			Element AnnotationRef_element = (Element) AnnotationRef_nodeList.item(i);
			AnnotationRef annotationList_reference = new AnnotationRef();
			annotationList_reference.setID(AnnotationRef_element.getAttribute("ID"));
			model.addReference(this, annotationList_reference);
		}
	}

	// -- Plane API methods --

	public void link(Reference reference, OMEModelObject o)
	{
		if (reference instanceof AnnotationRef)
		{
			Annotation o_casted = (Annotation) o;
			o_casted.linkPlane(this);
			annotationList.add(o_casted);
		}
		// TODO: Should be its own Exception
		throw new RuntimeException(
				"Unable to handle reference of type: " + reference.getClass());
	}


	// Property
	public Double getExposureTime()
	{
		return exposureTime;
	}

	public void setExposureTime(Double exposureTime)
	{
		this.exposureTime = exposureTime;
	}

	// Property
	public Double getPositionZ()
	{
		return positionZ;
	}

	public void setPositionZ(Double positionZ)
	{
		this.positionZ = positionZ;
	}

	// Property
	public Double getPositionX()
	{
		return positionX;
	}

	public void setPositionX(Double positionX)
	{
		this.positionX = positionX;
	}

	// Property
	public Double getPositionY()
	{
		return positionY;
	}

	public void setPositionY(Double positionY)
	{
		this.positionY = positionY;
	}

	// Property
	public Double getDeltaT()
	{
		return deltaT;
	}

	public void setDeltaT(Double deltaT)
	{
		this.deltaT = deltaT;
	}

	// Property
	public Integer getTheC()
	{
		return theC;
	}

	public void setTheC(Integer theC)
	{
		this.theC = theC;
	}

	// Property
	public Integer getTheZ()
	{
		return theZ;
	}

	public void setTheZ(Integer theZ)
	{
		this.theZ = theZ;
	}

	// Property
	public Integer getTheT()
	{
		return theT;
	}

	public void setTheT(Integer theT)
	{
		this.theT = theT;
	}

	// Property
	public String getHashSHA1()
	{
		return hashSHA1;
	}

	public void setHashSHA1(String hashSHA1)
	{
		this.hashSHA1 = hashSHA1;
	}

	// Reference which occurs more than once
	public int sizeOfLinkedAnnotationList()
	{
		return annotationList.size();
	}

	public List<Annotation> copyLinkedAnnotationList()
	{
		return new ArrayList<Annotation>(annotationList);
	}

	public Annotation getLinkedAnnotation(int index)
	{
		return annotationList.get(index);
	}

	public Annotation setLinkedAnnotation(int index, Annotation o)
	{
		return annotationList.set(index, o);
	}

	public boolean linkAnnotation(Annotation o)
	{
		o.linkPlane(this);
		return annotationList.add(o);
	}

	public boolean unlinkAnnotation(Annotation o)
	{
		o.unlinkPlane(this);
		return annotationList.remove(o);
	}

	public Element asXMLElement(Document document)
	{
		return asXMLElement(document, null);
	}

	protected Element asXMLElement(Document document, Element Plane_element)
	{
		// Creating XML block for Plane
		if (Plane_element == null)
		{
			Plane_element =
					document.createElementNS(NAMESPACE, "Plane");
		}

		if (exposureTime != null)
		{
			// Attribute property ExposureTime
			Plane_element.setAttribute("ExposureTime", exposureTime.toString());
		}
		if (positionZ != null)
		{
			// Attribute property PositionZ
			Plane_element.setAttribute("PositionZ", positionZ.toString());
		}
		if (positionX != null)
		{
			// Attribute property PositionX
			Plane_element.setAttribute("PositionX", positionX.toString());
		}
		if (positionY != null)
		{
			// Attribute property PositionY
			Plane_element.setAttribute("PositionY", positionY.toString());
		}
		if (deltaT != null)
		{
			// Attribute property DeltaT
			Plane_element.setAttribute("DeltaT", deltaT.toString());
		}
		if (theC != null)
		{
			// Attribute property TheC
			Plane_element.setAttribute("TheC", theC.toString());
		}
		if (theZ != null)
		{
			// Attribute property TheZ
			Plane_element.setAttribute("TheZ", theZ.toString());
		}
		if (theT != null)
		{
			// Attribute property TheT
			Plane_element.setAttribute("TheT", theT.toString());
		}
		if (hashSHA1 != null)
		{
			// Element property HashSHA1 which is not complex (has no
			// sub-elements)
			Element hashSHA1_element = 
					document.createElementNS(NAMESPACE, "HashSHA1");
			hashSHA1_element.setTextContent(hashSHA1);
			Plane_element.appendChild(hashSHA1_element);
		}
		if (annotationList != null)
		{
			// Reference property AnnotationRef which occurs more than once
			for (Annotation annotationList_value : annotationList)
			{
				AnnotationRef o = new AnnotationRef();
				o.setID(annotationList_value.getID());
				Plane_element.appendChild(o.asXMLElement(document));
			}
		}
		return super.asXMLElement(document, Plane_element);
	}
}
