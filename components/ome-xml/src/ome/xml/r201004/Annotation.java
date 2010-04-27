/*
 * ome.xml.r201004.Annotation
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
 * Created by callan via xsd-fu on 2010-04-27 09:58:45+0100
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
import ome.xml.r201004.primitives.*;

public abstract class Annotation extends AbstractOMEModelObject
{
	// -- Constants --

	public static final String NAMESPACE = "http://www.openmicroscopy.org/Schemas/SA/2010-04";

	// -- Instance variables --

	// Property
	private String namespace;

	// Property
	private String id;

	// Back reference Image_BackReference
	private List<Image> image_BackReferenceList = new ArrayList<Image>();

	// Back reference Pixels_BackReference
	private List<Pixels> pixels_BackReferenceList = new ArrayList<Pixels>();

	// Back reference Plane_BackReference
	private List<Plane> plane_BackReferenceList = new ArrayList<Plane>();

	// Back reference Channel_BackReference
	private List<Channel> channel_BackReferenceList = new ArrayList<Channel>();

	// Back reference Project_BackReference
	private List<Project> project_BackReferenceList = new ArrayList<Project>();

	// Back reference Dataset_BackReference
	private List<Dataset> dataset_BackReferenceList = new ArrayList<Dataset>();

	// Back reference Experimenter_BackReference
	private List<Experimenter> experimenter_BackReferenceList = new ArrayList<Experimenter>();

	// Back reference Plate_BackReference
	private List<Plate> plate_BackReferenceList = new ArrayList<Plate>();

	// Back reference Reagent_BackReference
	private List<Reagent> reagent_BackReferenceList = new ArrayList<Reagent>();

	// Back reference Screen_BackReference
	private List<Screen> screen_BackReferenceList = new ArrayList<Screen>();

	// Back reference PlateAcquisition_BackReference
	private List<PlateAcquisition> plateAcquisition_BackReferenceList = new ArrayList<PlateAcquisition>();

	// Back reference Well_BackReference
	private List<Well> well_BackReferenceList = new ArrayList<Well>();

	// Back reference WellSample_BackReference
	private List<WellSample> wellSample_BackReferenceList = new ArrayList<WellSample>();

	// Back reference ROI_BackReference
	private List<ROI> roi_backReferenceList = new ArrayList<ROI>();

	// Back reference Shape_BackReference
	private List<Shape> shape_BackReferenceList = new ArrayList<Shape>();

	// Back reference ListAnnotation_BackReference
	private List<ListAnnotation> listAnnotation_BackReferenceList = new ArrayList<ListAnnotation>();

	// -- Constructors --

	/** Default constructor. */
	public Annotation()
	{
		super();
	}

	/** 
	 * Constructs Annotation recursively from an XML DOM tree.
	 * @param element Root of the XML DOM tree to construct a model object
	 * graph from.
	 * @param model Handler for the OME model which keeps track of instances
	 * and references seen during object population.
	 * @throws EnumerationException If there is an error instantiating an
	 * enumeration during model object creation.
	 */
	public Annotation(Element element, OMEModel model)
	    throws EnumerationException
	{
		update(element, model);
	}

	// -- Custom content from Annotation specific template --


	// -- OMEModelObject API methods --

	/** 
	 * Updates Annotation recursively from an XML DOM tree. <b>NOTE:</b> No
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
		if (!"Annotation".equals(tagName))
		{
			System.err.println(String.format(
					"WARNING: Expecting node name of Annotation got %s",
					tagName));
			// TODO: Should be its own Exception
			//throw new RuntimeException(String.format(
			//		"Expecting node name of Annotation got %s",
			//		tagName));
		}
		if (element.hasAttribute("Namespace"))
		{
			// Attribute property Namespace
			setNamespace(String.valueOf(
					element.getAttribute("Namespace")));
		}
		if (!element.hasAttribute("ID") && getID() == null)
		{
			// TODO: Should be its own exception
			throw new RuntimeException(String.format(
					"Annotation missing required ID property."));
		}
		if (element.hasAttribute("ID"))
		{
			// ID property
			setID(String.valueOf(
						element.getAttribute("ID")));
			// Adding this model object to the model handler
		    	model.addModelObject(getID(), this);
		}
		// *** IGNORING *** Skipped back reference Image_BackReference
		// *** IGNORING *** Skipped back reference Pixels_BackReference
		// *** IGNORING *** Skipped back reference Plane_BackReference
		// *** IGNORING *** Skipped back reference Channel_BackReference
		// *** IGNORING *** Skipped back reference Project_BackReference
		// *** IGNORING *** Skipped back reference Dataset_BackReference
		// *** IGNORING *** Skipped back reference Experimenter_BackReference
		// *** IGNORING *** Skipped back reference Plate_BackReference
		// *** IGNORING *** Skipped back reference Reagent_BackReference
		// *** IGNORING *** Skipped back reference Screen_BackReference
		// *** IGNORING *** Skipped back reference PlateAcquisition_BackReference
		// *** IGNORING *** Skipped back reference Well_BackReference
		// *** IGNORING *** Skipped back reference WellSample_BackReference
		// *** IGNORING *** Skipped back reference ROI_BackReference
		// *** IGNORING *** Skipped back reference Shape_BackReference
		// *** IGNORING *** Skipped back reference ListAnnotation_BackReference
	}

	// -- Annotation API methods --

	public void link(Reference reference, OMEModelObject o)
	{
		// TODO: Should be its own Exception
		throw new RuntimeException(
				"Unable to handle reference of type: " + reference.getClass());
	}


	// Property
	public String getNamespace()
	{
		return namespace;
	}

	public void setNamespace(String namespace)
	{
		this.namespace = namespace;
	}

	// Property
	public String getID()
	{
		return id;
	}

	public void setID(String id)
	{
		this.id = id;
	}

	// Reference which occurs more than once
	public int sizeOfLinkedImageList()
	{
		return image_BackReferenceList.size();
	}

	public List<Image> copyLinkedImageList()
	{
		return new ArrayList<Image>(image_BackReferenceList);
	}

	public Image getLinkedImage(int index)
	{
		return image_BackReferenceList.get(index);
	}

	public Image setLinkedImage(int index, Image o)
	{
		return image_BackReferenceList.set(index, o);
	}

	public boolean linkImage(Image o)
	{
		return image_BackReferenceList.add(o);
	}

	public boolean unlinkImage(Image o)
	{
		return image_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedPixelsList()
	{
		return pixels_BackReferenceList.size();
	}

	public List<Pixels> copyLinkedPixelsList()
	{
		return new ArrayList<Pixels>(pixels_BackReferenceList);
	}

	public Pixels getLinkedPixels(int index)
	{
		return pixels_BackReferenceList.get(index);
	}

	public Pixels setLinkedPixels(int index, Pixels o)
	{
		return pixels_BackReferenceList.set(index, o);
	}

	public boolean linkPixels(Pixels o)
	{
		return pixels_BackReferenceList.add(o);
	}

	public boolean unlinkPixels(Pixels o)
	{
		return pixels_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedPlaneList()
	{
		return plane_BackReferenceList.size();
	}

	public List<Plane> copyLinkedPlaneList()
	{
		return new ArrayList<Plane>(plane_BackReferenceList);
	}

	public Plane getLinkedPlane(int index)
	{
		return plane_BackReferenceList.get(index);
	}

	public Plane setLinkedPlane(int index, Plane o)
	{
		return plane_BackReferenceList.set(index, o);
	}

	public boolean linkPlane(Plane o)
	{
		return plane_BackReferenceList.add(o);
	}

	public boolean unlinkPlane(Plane o)
	{
		return plane_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedChannelList()
	{
		return channel_BackReferenceList.size();
	}

	public List<Channel> copyLinkedChannelList()
	{
		return new ArrayList<Channel>(channel_BackReferenceList);
	}

	public Channel getLinkedChannel(int index)
	{
		return channel_BackReferenceList.get(index);
	}

	public Channel setLinkedChannel(int index, Channel o)
	{
		return channel_BackReferenceList.set(index, o);
	}

	public boolean linkChannel(Channel o)
	{
		return channel_BackReferenceList.add(o);
	}

	public boolean unlinkChannel(Channel o)
	{
		return channel_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedProjectList()
	{
		return project_BackReferenceList.size();
	}

	public List<Project> copyLinkedProjectList()
	{
		return new ArrayList<Project>(project_BackReferenceList);
	}

	public Project getLinkedProject(int index)
	{
		return project_BackReferenceList.get(index);
	}

	public Project setLinkedProject(int index, Project o)
	{
		return project_BackReferenceList.set(index, o);
	}

	public boolean linkProject(Project o)
	{
		return project_BackReferenceList.add(o);
	}

	public boolean unlinkProject(Project o)
	{
		return project_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedDatasetList()
	{
		return dataset_BackReferenceList.size();
	}

	public List<Dataset> copyLinkedDatasetList()
	{
		return new ArrayList<Dataset>(dataset_BackReferenceList);
	}

	public Dataset getLinkedDataset(int index)
	{
		return dataset_BackReferenceList.get(index);
	}

	public Dataset setLinkedDataset(int index, Dataset o)
	{
		return dataset_BackReferenceList.set(index, o);
	}

	public boolean linkDataset(Dataset o)
	{
		return dataset_BackReferenceList.add(o);
	}

	public boolean unlinkDataset(Dataset o)
	{
		return dataset_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedExperimenterList()
	{
		return experimenter_BackReferenceList.size();
	}

	public List<Experimenter> copyLinkedExperimenterList()
	{
		return new ArrayList<Experimenter>(experimenter_BackReferenceList);
	}

	public Experimenter getLinkedExperimenter(int index)
	{
		return experimenter_BackReferenceList.get(index);
	}

	public Experimenter setLinkedExperimenter(int index, Experimenter o)
	{
		return experimenter_BackReferenceList.set(index, o);
	}

	public boolean linkExperimenter(Experimenter o)
	{
		return experimenter_BackReferenceList.add(o);
	}

	public boolean unlinkExperimenter(Experimenter o)
	{
		return experimenter_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedPlateList()
	{
		return plate_BackReferenceList.size();
	}

	public List<Plate> copyLinkedPlateList()
	{
		return new ArrayList<Plate>(plate_BackReferenceList);
	}

	public Plate getLinkedPlate(int index)
	{
		return plate_BackReferenceList.get(index);
	}

	public Plate setLinkedPlate(int index, Plate o)
	{
		return plate_BackReferenceList.set(index, o);
	}

	public boolean linkPlate(Plate o)
	{
		return plate_BackReferenceList.add(o);
	}

	public boolean unlinkPlate(Plate o)
	{
		return plate_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedReagentList()
	{
		return reagent_BackReferenceList.size();
	}

	public List<Reagent> copyLinkedReagentList()
	{
		return new ArrayList<Reagent>(reagent_BackReferenceList);
	}

	public Reagent getLinkedReagent(int index)
	{
		return reagent_BackReferenceList.get(index);
	}

	public Reagent setLinkedReagent(int index, Reagent o)
	{
		return reagent_BackReferenceList.set(index, o);
	}

	public boolean linkReagent(Reagent o)
	{
		return reagent_BackReferenceList.add(o);
	}

	public boolean unlinkReagent(Reagent o)
	{
		return reagent_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedScreenList()
	{
		return screen_BackReferenceList.size();
	}

	public List<Screen> copyLinkedScreenList()
	{
		return new ArrayList<Screen>(screen_BackReferenceList);
	}

	public Screen getLinkedScreen(int index)
	{
		return screen_BackReferenceList.get(index);
	}

	public Screen setLinkedScreen(int index, Screen o)
	{
		return screen_BackReferenceList.set(index, o);
	}

	public boolean linkScreen(Screen o)
	{
		return screen_BackReferenceList.add(o);
	}

	public boolean unlinkScreen(Screen o)
	{
		return screen_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedPlateAcquisitionList()
	{
		return plateAcquisition_BackReferenceList.size();
	}

	public List<PlateAcquisition> copyLinkedPlateAcquisitionList()
	{
		return new ArrayList<PlateAcquisition>(plateAcquisition_BackReferenceList);
	}

	public PlateAcquisition getLinkedPlateAcquisition(int index)
	{
		return plateAcquisition_BackReferenceList.get(index);
	}

	public PlateAcquisition setLinkedPlateAcquisition(int index, PlateAcquisition o)
	{
		return plateAcquisition_BackReferenceList.set(index, o);
	}

	public boolean linkPlateAcquisition(PlateAcquisition o)
	{
		return plateAcquisition_BackReferenceList.add(o);
	}

	public boolean unlinkPlateAcquisition(PlateAcquisition o)
	{
		return plateAcquisition_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedWellList()
	{
		return well_BackReferenceList.size();
	}

	public List<Well> copyLinkedWellList()
	{
		return new ArrayList<Well>(well_BackReferenceList);
	}

	public Well getLinkedWell(int index)
	{
		return well_BackReferenceList.get(index);
	}

	public Well setLinkedWell(int index, Well o)
	{
		return well_BackReferenceList.set(index, o);
	}

	public boolean linkWell(Well o)
	{
		return well_BackReferenceList.add(o);
	}

	public boolean unlinkWell(Well o)
	{
		return well_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedWellSampleList()
	{
		return wellSample_BackReferenceList.size();
	}

	public List<WellSample> copyLinkedWellSampleList()
	{
		return new ArrayList<WellSample>(wellSample_BackReferenceList);
	}

	public WellSample getLinkedWellSample(int index)
	{
		return wellSample_BackReferenceList.get(index);
	}

	public WellSample setLinkedWellSample(int index, WellSample o)
	{
		return wellSample_BackReferenceList.set(index, o);
	}

	public boolean linkWellSample(WellSample o)
	{
		return wellSample_BackReferenceList.add(o);
	}

	public boolean unlinkWellSample(WellSample o)
	{
		return wellSample_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedROIList()
	{
		return roi_backReferenceList.size();
	}

	public List<ROI> copyLinkedROIList()
	{
		return new ArrayList<ROI>(roi_backReferenceList);
	}

	public ROI getLinkedROI(int index)
	{
		return roi_backReferenceList.get(index);
	}

	public ROI setLinkedROI(int index, ROI o)
	{
		return roi_backReferenceList.set(index, o);
	}

	public boolean linkROI(ROI o)
	{
		return roi_backReferenceList.add(o);
	}

	public boolean unlinkROI(ROI o)
	{
		return roi_backReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedShapeList()
	{
		return shape_BackReferenceList.size();
	}

	public List<Shape> copyLinkedShapeList()
	{
		return new ArrayList<Shape>(shape_BackReferenceList);
	}

	public Shape getLinkedShape(int index)
	{
		return shape_BackReferenceList.get(index);
	}

	public Shape setLinkedShape(int index, Shape o)
	{
		return shape_BackReferenceList.set(index, o);
	}

	public boolean linkShape(Shape o)
	{
		return shape_BackReferenceList.add(o);
	}

	public boolean unlinkShape(Shape o)
	{
		return shape_BackReferenceList.remove(o);
	}

	// Reference which occurs more than once
	public int sizeOfLinkedListAnnotationList()
	{
		return listAnnotation_BackReferenceList.size();
	}

	public List<ListAnnotation> copyLinkedListAnnotationList()
	{
		return new ArrayList<ListAnnotation>(listAnnotation_BackReferenceList);
	}

	public ListAnnotation getLinkedListAnnotation(int index)
	{
		return listAnnotation_BackReferenceList.get(index);
	}

	public ListAnnotation setLinkedListAnnotation(int index, ListAnnotation o)
	{
		return listAnnotation_BackReferenceList.set(index, o);
	}

	public boolean linkListAnnotation(ListAnnotation o)
	{
		return listAnnotation_BackReferenceList.add(o);
	}

	public boolean unlinkListAnnotation(ListAnnotation o)
	{
		return listAnnotation_BackReferenceList.remove(o);
	}

	public Element asXMLElement(Document document)
	{
		return asXMLElement(document, null);
	}

	protected Element asXMLElement(Document document, Element Annotation_element)
	{
		// Creating XML block for Annotation
		if (Annotation_element == null)
		{
			Annotation_element =
					document.createElementNS(NAMESPACE, "Annotation");
		}

		if (namespace != null)
		{
			// Attribute property Namespace
			Annotation_element.setAttribute("Namespace", namespace.toString());
		}
		if (id != null)
		{
			// Attribute property ID
			Annotation_element.setAttribute("ID", id.toString());
		}
		if (image_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Image_BackReference
		}
		if (pixels_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Pixels_BackReference
		}
		if (plane_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Plane_BackReference
		}
		if (channel_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Channel_BackReference
		}
		if (project_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Project_BackReference
		}
		if (dataset_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Dataset_BackReference
		}
		if (experimenter_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Experimenter_BackReference
		}
		if (plate_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Plate_BackReference
		}
		if (reagent_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Reagent_BackReference
		}
		if (screen_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Screen_BackReference
		}
		if (plateAcquisition_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference PlateAcquisition_BackReference
		}
		if (well_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Well_BackReference
		}
		if (wellSample_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference WellSample_BackReference
		}
		if (roi_backReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference ROI_BackReference
		}
		if (shape_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference Shape_BackReference
		}
		if (listAnnotation_BackReferenceList != null)
		{
			// *** IGNORING *** Skipped back reference ListAnnotation_BackReference
		}
		return super.asXMLElement(document, Annotation_element);
	}
}
